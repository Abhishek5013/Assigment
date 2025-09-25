# my_solver.py
from Test_placement_solver_ver2 import validate_placement, score_placement, plot_placement

BOARD_W, BOARD_H = 50, 50
BOARD_CENTER = (25, 25)

def center_of_mass(placement):
    total_area, sum_x, sum_y = 0, 0, 0
    for comp in placement.values():
        cx = comp['x'] + comp['w'] / 2
        cy = comp['y'] + comp['h'] / 2
        area = comp['w'] * comp['h']
        sum_x += cx * area
        sum_y += cy * area
        total_area += area
    return sum_x / total_area, sum_y / total_area

def solve():
    # Step 1: Fixed edge placements
    mb1 = {'x': 0, 'y': (BOARD_H - 15) // 2, 'w': 5, 'h': 15}             # Left
    mb2 = {'x': BOARD_W - 5, 'y': (BOARD_H - 15) // 2, 'w': 5, 'h': 15}   # Right
    usb = {'x': (BOARD_W - 5) // 2, 'y': 0, 'w': 5, 'h': 5}               # Top center

    # Step 2: Start microcontroller near center
    mc_x, mc_y = (BOARD_W // 2) - 2, (BOARD_H // 2) - 2

    # Step 3: Iteratively adjust microcontroller for COM balance
    best_micro, best_crystal, best_dist = None, None, 999
    for dx in range(-5, 6):
        for dy in range(-5, 6):
            micro = {'x': mc_x + dx, 'y': mc_y + dy, 'w': 5, 'h': 5}
            crystal = {'x': micro['x'], 'y': micro['y'] + 8, 'w': 5, 'h': 5}
            if crystal['y'] > BOARD_H - 5:
                crystal['y'] = micro['y'] - 8
            placement = {
                'USB_CONNECTOR': usb,
                'MIKROBUS_CONNECTOR_1': mb1,
                'MIKROBUS_CONNECTOR_2': mb2,
                'MICROCONTROLLER': micro,
                'CRYSTAL': crystal,
            }
            cx, cy = center_of_mass(placement)
            dist = ((cx - BOARD_CENTER[0]) ** 2 + (cy - BOARD_CENTER[1]) ** 2) ** 0.5
            if dist < best_dist:
                best_micro, best_crystal, best_dist = micro, crystal, dist

    # Final placement
    placement = {
        'USB_CONNECTOR': usb,
        'MIKROBUS_CONNECTOR_1': mb1,
        'MIKROBUS_CONNECTOR_2': mb2,
        'MICROCONTROLLER': best_micro,
        'CRYSTAL': best_crystal,
    }
    return placement


if __name__ == "__main__":
    placement = solve()
    if validate_placement(placement):
        print("\n✅ Valid placement found with balanced COM")
        score_placement(placement)
        plot_placement(placement)
    else:
        print("\n❌ Solver failed. Placement invalid.")

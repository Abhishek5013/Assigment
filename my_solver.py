# my_solver.py
# This is your main solver script for the assignment

from Test_placement_solver_ver2 import validate_placement, score_placement, plot_placement

# Example placement dictionary (components with x, y, width, height)
placement = {
    'USB_CONNECTOR':        {'x': 20, 'y': 45, 'w': 5, 'h': 5},   # USB at bottom edge
    'MIKROBUS_CONNECTOR_1': {'x': 0, 'y': 15, 'w': 5, 'h': 15},   # MikroBus 1 on left edge
    'MIKROBUS_CONNECTOR_2': {'x': 45, 'y': 15, 'w': 5, 'h': 15},  # MikroBus 2 on right edge
    'MICROCONTROLLER':      {'x': 22, 'y': 22, 'w': 5, 'h': 5},   # Microcontroller near center
    'CRYSTAL':              {'x': 25, 'y': 14, 'w': 5, 'h': 5},   # Crystal close to microcontroller
}

# Run validator
if validate_placement(placement):
    print("\n✅ Placement is valid!")
    score_placement(placement)
    plot_placement(placement)
else:
    print("\n❌ Placement is invalid!")
    plot_placement(placement)

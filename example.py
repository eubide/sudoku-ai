from sudoku import Sudoku

# Create an empty board
game = Sudoku()

# Set some values
game.set_value(0, 0, 5)  # Set 5 in the top-left corner
game.set_value(1, 4, 6)  # Set 6 in the middle of second row

# Print the board
print("Current board:")
print(game)

# Try an invalid move
success = game.set_value(0, 1, 5)  # Try to put another 5 in first row
print("\nTrying to put 5 in first row:", "Succeeded" if success else "Failed")

# Clear a cell
game.clear_cell(0, 0)
print("\nAfter clearing (0,0):")
print(game)

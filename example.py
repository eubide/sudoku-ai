from sudoku import Sudoku

# Create an empty board
game = Sudoku()

# Set some values
game.set_value(0, 0, 5)  # Set 5 in the top-left corner
print(game)
game.set_value(1, 4, 6)  # Set 6 in the middle of second row
print(game)

# Print the board
print("Current board:")
print(game)

# Try an invalid move
success = game.set_value(6, 8, 5)  # Try to put another 5 in first row
print("\nTrying to put 5 in the first row:", "Success" if success else "Failure")

# Clear a cell
game.clear_cell(0, 0)
print("\nAfter clearing (0,0):")
print(game)


# This will raise ValueError because the 5 is repeated in the first row
invalid_board = [
    [5, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
invalid_game = Sudoku(invalid_board)  # This will raise ValueError


generator = SudokuGenerator()
puzzle, solution = generator.generate(num_clues=25)  # Genera un puzzle con 25 pistas

print("Puzzle generado:")
print(puzzle)
print("\nSolución:")
print(Sudoku(solution))
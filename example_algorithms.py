from sudoku_algorithms import SudokuAlgorithms
from sudoku_generator import SudokuGenerator
import numpy as np

# Example Sudoku board (0 represents empty cells)
board = np.array(
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
)

solver = SudokuAlgorithms(board.copy())
print("Resolviendo con backtracking...")
solver.solve_backtracking()

solver = SudokuAlgorithms(board.copy())
print("Resolviendo con algoritmo estocástico...")
solver.solve_stochastic()

solver = SudokuAlgorithms(board.copy())
print("Resolviendo con propagación de restricciones...")
solver.solve_constraint_propagation()

solver = SudokuAlgorithms(board.copy())
print("Resolviendo con propagación de restricciones...")
solver.solve_dlx()

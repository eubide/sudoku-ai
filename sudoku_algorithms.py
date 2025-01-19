import numpy as np
from sudoku_visual_solver import SudokuVisualSolver
import matplotlib.pyplot as plt
import random


class SudokuAlgorithms(SudokuVisualSolver):
    def __init__(self, board=None):
        super().__init__(board)

    def solve_stochastic(self):
        """Solve Sudoku using a stochastic approach (random sampling with backtracking)"""
        self._draw_grid("Stochastic Algorithm")
        plt.pause(self.delay)

        def solve_recursive(row=0, col=0):
            if col == 9:
                row += 1
                col = 0
            if row == 9:
                return True

            if self.board[row, col] != 0:
                return solve_recursive(row, col + 1)

            self.highlight_cell(row, col)
            plt.pause(self.delay / 2)

            # Try numbers in random order
            numbers = list(range(1, 10))
            random.shuffle(numbers)

            for num in numbers:
                if self.is_valid_move(row, col, num):
                    self.board[row, col] = num
                    self.steps += 1
                    self._draw_grid("Stochastic Algorithm")
                    self.highlight_cell(row, col, color="green", alpha=0.2)
                    plt.pause(self.delay)

                    if solve_recursive(row, col + 1):
                        return True

                    self.board[row, col] = 0
                    self._draw_grid("Stochastic Algorithm")
                    self.highlight_cell(row, col, color="red", alpha=0.2)
                    plt.pause(self.delay)

            return False

        if solve_recursive():
            plt.title("Sudoku solved with stochastic approach!")
        else:
            plt.title("No solution possible")
        plt.show()

    def solve_constraint_propagation(self):
        """Solve Sudoku using constraint propagation (looking ahead)"""
        self._draw_grid("Constraint Propagation")
        plt.pause(self.delay)

        def get_possible_values(row, col):
            """Get all possible values for a cell"""
            values = set(range(1, 10))
            # Remove values from row
            values -= set(self.board[row])
            # Remove values from column
            values -= set(self.board[:, col])
            # Remove values from 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            values -= set(
                self.board[box_row : box_row + 3, box_col : box_col + 3].flatten()
            )
            return values

        def find_min_possibilities():
            """Find empty cell with fewest possible values"""
            min_len = 10
            min_pos = None

            for i in range(9):
                for j in range(9):
                    if self.board[i, j] == 0:
                        possible = get_possible_values(i, j)
                        if len(possible) < min_len:
                            min_len = len(possible)
                            min_pos = (i, j, possible)

            return min_pos

        def solve_recursive():
            cell = find_min_possibilities()
            if not cell:
                return True

            row, col, possible = cell
            self.highlight_cell(row, col)
            plt.pause(self.delay / 2)

            for num in possible:
                if self.is_valid_move(row, col, num):
                    self.board[row, col] = num
                    self.steps += 1
                    self._draw_grid("Constraint Propagation")
                    self.highlight_cell(row, col, color="green", alpha=0.2)
                    plt.pause(self.delay)

                    if solve_recursive():
                        return True

                    self.board[row, col] = 0
                    self._draw_grid("Constraint Propagation")
                    self.highlight_cell(row, col, color="red", alpha=0.2)
                    plt.pause(self.delay)

            return False

        if solve_recursive():
            plt.title("Sudoku solved with constraint propagation!")
        else:
            plt.title("No solution possible")
        plt.show()

    def solve_backtracking(self):
        """Solve Sudoku using simple backtracking"""
        self._draw_grid("Backtracking")
        plt.pause(self.delay)

        def solve_recursive(row=0, col=0):
            if col == 9:
                row += 1
                col = 0
            if row == 9:
                return True

            if self.board[row, col] != 0:
                return solve_recursive(row, col + 1)

            self.highlight_cell(row, col)
            plt.pause(self.delay / 2)

            for num in range(1, 10):
                if self.is_valid_move(row, col, num):
                    self.board[row, col] = num
                    self.steps += 1
                    self._draw_grid("Backtracking")
                    self.highlight_cell(row, col, color="green", alpha=0.2)
                    plt.pause(self.delay)

                    if solve_recursive(row, col + 1):
                        return True

                    self.board[row, col] = 0
                    self._draw_grid("Backtracking")
                    self.highlight_cell(row, col, color="red", alpha=0.2)
                    plt.pause(self.delay)

            return False

        if solve_recursive():
            plt.title("Sudoku solved with backtracking!")
        else:
            plt.title("No solution possible")
        plt.show()

    def solve_dlx(self):
        """Solve Sudoku using Dancing Links (Algorithm X)"""
        self._draw_grid("Dancing Links (Algorithm X)")
        plt.pause(self.delay)

        def create_cover_matrix():
            # Create the initial cover matrix for the exact cover problem
            n = 9
            cover_matrix = []

            # For each cell in the grid
            for r in range(n):
                for c in range(n):
                    # For each possible digit
                    for num in range(1, n + 1):
                        if self.board[r, c] == 0 or self.board[r, c] == num:
                            # Add constraints for cell, row, column and box
                            b = (r // 3) * 3 + c // 3
                            row = [0] * (4 * n * n)
                            row[r * n + c] = 1  # Cell constraint
                            row[n * n + r * n + num - 1] = 1  # Row constraint
                            row[2 * n * n + c * n + num - 1] = 1  # Column constraint
                            row[3 * n * n + b * n + num - 1] = 1  # Box constraint
                            cover_matrix.append((r, c, num, row))
            return cover_matrix

        def select_column(matrix):
            # Select column with minimum number of 1s
            min_count = float("inf")
            selected = None
            for j in range(len(matrix[0])):
                count = sum(row[j] for row in matrix)
                if 0 < count < min_count:
                    min_count = count
                    selected = j
            return selected

        def solve_exact_cover(matrix, solution):
            if not matrix:
                return True

            col = select_column(matrix)
            if col is None:
                return False

            # Try each row that has a 1 in the selected column
            for i, row in enumerate(matrix):
                if row[col] == 1:
                    r, c, num = solution[i]
                    self.board[r, c] = num
                    self.steps += 1
                    self._draw_grid("Dancing Links (Algorithm X)")
                    self.highlight_cell(r, c, color="green", alpha=0.2)
                    plt.pause(self.delay)

                    # Remove rows and columns
                    new_matrix = []
                    new_solution = []
                    covered_cols = set()
                    for j, val in enumerate(row):
                        if val == 1:
                            covered_cols.add(j)

                    for k, (other_row, sol) in enumerate(zip(matrix, solution)):
                        if k != i and not any(other_row[j] == 1 for j in covered_cols):
                            new_row = [
                                v
                                for j, v in enumerate(other_row)
                                if j not in covered_cols
                            ]
                            new_matrix.append(new_row)
                            new_solution.append(sol)

                    if solve_exact_cover(new_matrix, new_solution):
                        return True

                    self.board[r, c] = 0
                    self._draw_grid("Dancing Links (Algorithm X)")
                    self.highlight_cell(r, c, color="red", alpha=0.2)
                    plt.pause(self.delay)

            return False

        # Initialize the exact cover problem
        cover = create_cover_matrix()
        matrix = [row[-1] for row in cover]
        solution = [(r, c, num) for r, c, num, _ in cover]

        if solve_exact_cover(matrix, solution):
            plt.title("Sudoku solved with Dancing Links!")
        else:
            plt.title("No solution possible")
        plt.show()

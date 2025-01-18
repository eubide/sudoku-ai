import numpy as np
from sudoku import Sudoku
import random


class SudokuGenerator:
    def __init__(self):
        self.sudoku = Sudoku()

    def _fill_diagonal_blocks(self):
        """Fill the three diagonal 3x3 blocks with random numbers."""
        numbers = list(range(1, 10))
        for i in range(0, 9, 3):
            # Shuffle numbers for each diagonal block
            random.shuffle(numbers)
            pos = 0
            for row in range(i, i + 3):
                for col in range(i, i + 3):
                    self.sudoku.board[row, col] = numbers[pos]
                    pos += 1

    def _solve(self, row=0, col=0):
        """
        Solve the Sudoku using backtracking.
        Returns True if a solution is found, False otherwise.
        """
        if col == 9:
            row += 1
            col = 0
        if row == 9:
            return True

        if self.sudoku.board[row, col] != 0:
            return self._solve(row, col + 1)

        numbers = list(range(1, 10))
        random.shuffle(numbers)  # Try numbers in random order

        for num in numbers:
            if self.sudoku.is_valid_move(row, col, num):
                self.sudoku.board[row, col] = num
                if self._solve(row, col + 1):
                    return True
                self.sudoku.board[row, col] = 0

        return False

    def generate(self, num_clues=25):
        """
        Generate a new Sudoku puzzle with the specified number of clues.

        Args:
            num_clues: Number of clues to leave in the puzzle (minimum 17)

        Returns:
            Sudoku: A new Sudoku instance with the generated puzzle

        Raises:
            ValueError: If num_clues is less than 17
        """
        if num_clues < 17:
            raise ValueError("A Sudoku puzzle must have at least 17 clues")

        # Start with empty board
        self.sudoku = Sudoku()

        # Fill diagonal blocks (this ensures we start with some valid numbers)
        self._fill_diagonal_blocks()

        # Solve the rest of the puzzle
        self._solve()

        # Create a copy of the solved board
        solution = self.sudoku.board.copy()

        # Remove numbers while keeping at least num_clues
        cells = list(range(81))  # All positions in the 9x9 grid
        random.shuffle(cells)

        for cell in cells[: (81 - num_clues)]:  # Remove (81 - num_clues) numbers
            row, col = cell // 9, cell % 9
            self.sudoku.board[row, col] = 0

        return self.sudoku, solution

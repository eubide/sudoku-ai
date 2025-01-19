import numpy as np
import matplotlib.pyplot as plt
from sudoku import Sudoku


class SudokuVisualSolver(Sudoku):
    def __init__(self, board=None):
        super().__init__(board)
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.delay = 0.0001  # Delay between steps in seconds
        self.steps = 0  # Initialize step counter

    def _draw_grid(self):
        """Draw the Sudoku grid with current numbers."""
        self.ax.clear()
        # Draw the main grid
        for i in range(10):
            lw = 2 if i % 3 == 0 else 0.5
            self.ax.axhline(y=i, color="black", linewidth=lw)
            self.ax.axvline(x=i, color="black", linewidth=lw)

        # Fill in the numbers
        for i in range(9):
            for j in range(9):
                if self.board[i, j] != 0:
                    self.ax.text(
                        j + 0.5,
                        8.5 - i,
                        str(int(self.board[i, j])),
                        ha="center",
                        va="center",
                    )

        # Add step counter text
        self.ax.text(4.5, -0.5, f"Steps: {self.steps}", ha="center", va="center")

        self.ax.set_xlim(0, 9)
        self.ax.set_ylim(0, 9)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        plt.pause(0.001)

    def highlight_cell(self, row, col, color="yellow", alpha=0.3):
        """Highlight a cell to show the current focus."""
        self.ax.add_patch(
            plt.Rectangle((col, 8 - row), 1, 1, facecolor=color, alpha=alpha)
        )

import numpy as np
import matplotlib.pyplot as plt
from sudoku import Sudoku


class SudokuVisualSolver(Sudoku):
    def __init__(self, board=None):
        super().__init__(board)
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.delay = 0.0001  # Delay between steps in seconds
        self.steps = 0  # Initialize step counter

    def _draw_grid(self, algorithm_name=None):
        """Draw the Sudoku grid with current numbers."""
        self.ax.clear()

        # Add algorithm name if provided
        if algorithm_name:
            self.ax.text(
                4.5,
                9.7,
                algorithm_name,
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
            )

        # Draw the main grid
        for i in range(10):
            lw = 2 if i % 3 == 0 else 0.5
            # Limitar las líneas horizontales al área del Sudoku (0-9)
            self.ax.plot([0, 9], [i, i], color="black", linewidth=lw)
            # Limitar las líneas verticales al área del Sudoku (0-9)
            self.ax.plot([i, i], [0, 9], color="black", linewidth=lw)

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
        self.ax.set_ylim(
            -1, 10.5
        )  # Adjusted to give more space to the title and counter
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        plt.pause(0.001)

    def highlight_cell(self, row, col, color="yellow", alpha=0.3):
        """Highlight a cell to show the current focus."""
        self.ax.add_patch(
            plt.Rectangle((col, 8 - row), 1, 1, facecolor=color, alpha=alpha)
        )

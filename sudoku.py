import numpy as np

class Sudoku:
    def __init__(self, board=None):
        """
        Initialize a Sudoku board.
        If no board is provided, creates an empty 9x9 board.
        
        Args:
            board: Optional list of lists or numpy array representing the initial board
                  Use 0 for empty cells
        """
        if board is None:
            self.board = np.zeros((9, 9), dtype=int)
        else:
            self.board = np.array(board, dtype=int)
            if self.board.shape != (9, 9):
                raise ValueError("Sudoku board must be 9x9")
    
    def get_row(self, row):
        """Get a specific row from the board."""
        return self.board[row].copy()
    
    def get_column(self, col):
        """Get a specific column from the board."""
        return self.board[:, col].copy()
    
    def get_block(self, row, col):
        """Get the 3x3 block that contains the cell at (row, col)."""
        block_row = (row // 3) * 3
        block_col = (col // 3) * 3
        return self.board[block_row:block_row + 3, block_col:block_col + 3].copy()
    
    def is_valid_move(self, row, col, num):
        """
        Check if placing number 'num' at position (row, col) is valid.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to check (1-9)
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        # Check if the cell is empty
        if self.board[row, col] != 0:
            return False
            
        # Check row
        if num in self.get_row(row):
            return False
            
        # Check column
        if num in self.get_column(col):
            return False
            
        # Check 3x3 block
        if num in self.get_block(row, col):
            return False
            
        return True
    
    def set_value(self, row, col, num):
        """
        Set a value in the board if it's a valid move.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
            
        Returns:
            bool: True if the value was set, False otherwise
        """
        if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
            return False
            
        if self.is_valid_move(row, col, num):
            self.board[row, col] = num
            return True
        return False
    
    def clear_cell(self, row, col):
        """Clear a cell by setting it to 0."""
        self.board[row, col] = 0
    
    def is_complete(self):
        """Check if the board is completely filled and valid."""
        if 0 in self.board:
            return False
            
        # Check all rows, columns and blocks
        for i in range(9):
            if not (set(self.get_row(i)) == set(range(1, 10)) and
                   set(self.get_column(i)) == set(range(1, 10))):
                return False
                
        # Check blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if set(self.get_block(i, j).flatten()) != set(range(1, 10)):
                    return False
                    
        return True
    
    def __str__(self):
        """Return a string representation of the board."""
        result = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                result += "-" * 21 + "\n"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    result += "| "
                result += str(self.board[i, j]) + " "
            result += "\n"
        return result

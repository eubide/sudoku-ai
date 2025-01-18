import numpy as np

class Sudoku:
    def __init__(self, board=None):
        """
        Initialize a Sudoku board.
        If no board is provided, creates an empty 9x9 board.
        
        Args:
            board: Optional list of lists or numpy array representing the initial board
                  Use 0 for empty cells
                  
        Raises:
            ValueError: If the board is not 9x9 or contains invalid numbers
                      or has repeated numbers in rows, columns or blocks
        """
        if board is None:
            self.board = np.zeros((9, 9), dtype=int)
        else:
            self.board = np.array(board, dtype=int)
            if self.board.shape != (9, 9):
                raise ValueError("Sudoku board must be 9x9")
            if not self._is_valid_board():
                raise ValueError("Invalid initial board: contains invalid numbers or repeated numbers in rows, columns or blocks")
    
    def get_row(self, row):
        """Get a specific row from the board."""
        return self.board[row]
    
    def get_column(self, col):
        """Get a specific column from the board."""
        return self.board[:, col]
    
    def get_block(self, row, col):
        """Get the 3x3 block that contains the cell at (row, col)."""
        block_row = (row // 3) * 3
        block_col = (col // 3) * 3
        return self.board[block_row:block_row + 3, block_col:block_col + 3]
    
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
        if num in self.get_block(row, col).flatten():
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
    
    def _is_valid_board(self):
        """
        Check if the initial board is valid.
        A valid board must:
        1. Contain only numbers from 0-9 (0 represents empty cells)
        2. Not have repeated numbers (1-9) in any row, column or 3x3 block
        
        Returns:
            bool: True if the board is valid, False otherwise
        """
        # Check if all numbers are in valid range (0-9)
        if not np.all((self.board >= 0) & (self.board <= 9)):
            return False
            
        # Check rows and columns
        for i in range(9):
            # Get non-zero numbers in row and column
            row_nums = self.get_row(i)[self.get_row(i) != 0]
            col_nums = self.get_column(i)[self.get_column(i) != 0]
            
            # Check for duplicates (if length of unique numbers is less than total numbers)
            if len(np.unique(row_nums)) < len(row_nums) or len(np.unique(col_nums)) < len(col_nums):
                return False
        
        # Check 3x3 blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = self.get_block(i, j)
                block_nums = block[block != 0]
                if len(np.unique(block_nums)) < len(block_nums):
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
                result += "- " if self.board[i, j] == 0 else str(self.board[i, j]) + " "
            result += "\n"
        return result

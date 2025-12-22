"""
Board class representing the game board.
Handles collision detection, line clearing, and board state.
"""

from typing import List, Tuple, Optional
from config import GRID_WIDTH, GRID_HEIGHT
from tetris.models.tetromino import Tetromino


class Board:
    """
    Represents the game board (playfield).
    Manages locked blocks, collision detection, and line clearing.
    """

    def __init__(self):
        """Initialize an empty board."""
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        # 2D grid: None = empty, color tuple = locked block
        self.grid: List[List[Optional[Tuple[int, int, int]]]] = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

    def is_valid_position(self, tetromino: Tetromino) -> bool:
        """
        Check if a tetromino is in a valid position.

        Args:
            tetromino: The tetromino to check

        Returns:
            True if the position is valid, False otherwise
        """
        for x, y in tetromino.get_blocks():
            # Check boundaries
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            # Check collision with locked blocks
            if self.grid[y][x] is not None:
                return False
        return True

    def lock_tetromino(self, tetromino: Tetromino) -> None:
        """
        Lock a tetromino in place on the board.

        Args:
            tetromino: The tetromino to lock
        """
        for x, y in tetromino.get_blocks():
            if 0 <= y < self.height and 0 <= x < self.width:
                self.grid[y][x] = tetromino.color

    def clear_lines(self) -> int:
        """
        Clear all complete lines and return the number cleared.

        Returns:
            Number of lines cleared
        """
        lines_to_clear = []

        # Find complete lines
        for y in range(self.height):
            if all(cell is not None for cell in self.grid[y]):
                lines_to_clear.append(y)

        # Remove complete lines and add empty lines at top
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [None for _ in range(self.width)])

        return len(lines_to_clear)

    def is_game_over(self) -> bool:
        """
        Check if the game is over (blocks reached the top).

        Returns:
            True if game is over, False otherwise
        """
        # Check if any blocks are in the top rows (spawn area)
        for x in range(self.width):
            if self.grid[0][x] is not None or self.grid[1][x] is not None:
                return True
        return False

    def get_cell(self, x: int, y: int) -> Optional[Tuple[int, int, int]]:
        """
        Get the color of a cell, or None if empty.

        Args:
            x: Column index
            y: Row index

        Returns:
            Color tuple (R, G, B) or None if empty
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.grid[y][x]
        return None

    def reset(self) -> None:
        """Clear the board."""
        self.grid = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

    def get_drop_distance(self, tetromino: Tetromino) -> int:
        """
        Calculate how far down a tetromino can drop.

        Args:
            tetromino: The tetromino to check

        Returns:
            Number of cells the tetromino can drop
        """
        distance = 0
        test_piece = tetromino.copy()

        while True:
            test_piece.move_down()
            if self.is_valid_position(test_piece):
                distance += 1
            else:
                break

        return distance

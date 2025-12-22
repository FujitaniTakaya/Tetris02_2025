"""
Tetromino class representing individual game pieces.
Handles piece shape, rotation, and position.
"""

import random
from typing import List, Tuple
from config import TETROMINO_SHAPES, TETROMINO_COLORS


class Tetromino:
    """
    Represents a single Tetromino piece.
    Encapsulates shape, color, position, and rotation state.
    """

    def __init__(self, shape_type: str, x: int = 0, y: int = 0):
        """
        Initialize a tetromino.

        Args:
            shape_type: Type of tetromino ('I', 'O', 'T', 'S', 'Z', 'J', 'L')
            x: Initial x position (column)
            y: Initial y position (row)
        """
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.rotation_state = 0
        self.color = TETROMINO_COLORS[shape_type]
        self.shapes = TETROMINO_SHAPES[shape_type]

    def get_blocks(self) -> List[Tuple[int, int]]:
        """
        Get the current block positions based on position and rotation.

        Returns:
            List of (x, y) positions for each block of the tetromino
        """
        current_shape = self.shapes[self.rotation_state]
        return [(self.x + dx, self.y + dy) for dx, dy in current_shape]

    def rotate_clockwise(self) -> None:
        """Rotate the tetromino 90 degrees clockwise."""
        self.rotation_state = (self.rotation_state + 1) % len(self.shapes)

    def rotate_counterclockwise(self) -> None:
        """Rotate the tetromino 90 degrees counterclockwise."""
        self.rotation_state = (self.rotation_state - 1) % len(self.shapes)

    def move(self, dx: int, dy: int) -> None:
        """
        Move the tetromino by the given offset.

        Args:
            dx: Change in x position
            dy: Change in y position
        """
        self.x += dx
        self.y += dy

    def move_left(self) -> None:
        """Move the tetromino one cell to the left."""
        self.move(-1, 0)

    def move_right(self) -> None:
        """Move the tetromino one cell to the right."""
        self.move(1, 0)

    def move_down(self) -> None:
        """Move the tetromino one cell down."""
        self.move(0, 1)

    def copy(self) -> 'Tetromino':
        """
        Create a copy of this tetromino.

        Returns:
            A new Tetromino instance with the same properties
        """
        new_piece = Tetromino(self.shape_type, self.x, self.y)
        new_piece.rotation_state = self.rotation_state
        return new_piece

    @staticmethod
    def create_random() -> 'Tetromino':
        """
        Create a random tetromino at the spawn position.

        Returns:
            A new random Tetromino instance
        """
        shape_type = random.choice(list(TETROMINO_SHAPES.keys()))
        return Tetromino(shape_type)

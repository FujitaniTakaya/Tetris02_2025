"""
Game class managing the core game logic and state.
"""

import random
from typing import Optional
from tetris.models.board import Board
from tetris.models.tetromino import Tetromino
from config import (
    GRID_WIDTH, SCORE_SINGLE_LINE, SCORE_DOUBLE_LINE,
    SCORE_TRIPLE_LINE, SCORE_TETRIS, SCORE_SOFT_DROP,
    SCORE_HARD_DROP, LINES_PER_LEVEL, INITIAL_FALL_SPEED,
    FALL_SPEED_DECREASE, MIN_FALL_SPEED
)


class Game:
    """
    Core game logic and state management.
    Follows single responsibility principle - only manages game rules and state.
    """

    def __init__(self):
        """Initialize the game state."""
        self.board = Board()
        self.current_piece: Optional[Tetromino] = None
        self.next_piece: Optional[Tetromino] = None
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.game_over = False
        self.paused = False

        # Spawn initial pieces
        self._spawn_new_piece()
        self.next_piece = Tetromino.create_random()

    def _spawn_new_piece(self) -> None:
        """Spawn a new tetromino at the top center of the board."""
        if self.next_piece:
            self.current_piece = self.next_piece
        else:
            self.current_piece = Tetromino.create_random()

        # Position at top center
        self.current_piece.x = GRID_WIDTH // 2 - 1
        self.current_piece.y = 0

        # Generate next piece
        self.next_piece = Tetromino.create_random()
        # Position next piece for preview
        self.next_piece.x = 0
        self.next_piece.y = 0

        # Check if spawn position is valid
        if not self.board.is_valid_position(self.current_piece):
            self.game_over = True

    def move_left(self) -> bool:
        """
        Attempt to move the current piece left.

        Returns:
            True if move was successful, False otherwise
        """
        if not self.current_piece or self.game_over or self.paused:
            return False

        self.current_piece.move_left()
        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.move_right()  # Undo move
            return False
        return True

    def move_right(self) -> bool:
        """
        Attempt to move the current piece right.

        Returns:
            True if move was successful, False otherwise
        """
        if not self.current_piece or self.game_over or self.paused:
            return False

        self.current_piece.move_right()
        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.move_left()  # Undo move
            return False
        return True

    def move_down(self) -> bool:
        """
        Attempt to move the current piece down.

        Returns:
            True if move was successful, False if piece locked
        """
        if not self.current_piece or self.game_over or self.paused:
            return False

        self.current_piece.move_down()
        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.move(0, -1)  # Undo move
            self._lock_piece()
            return False
        return True

    def soft_drop(self) -> int:
        """
        Move piece down and award points.

        Returns:
            Points earned from soft drop
        """
        if self.move_down():
            return SCORE_SOFT_DROP
        return 0

    def hard_drop(self) -> int:
        """
        Instantly drop piece to the bottom.

        Returns:
            Points earned from hard drop
        """
        if not self.current_piece or self.game_over or self.paused:
            return 0

        distance = self.board.get_drop_distance(self.current_piece)
        self.current_piece.move(0, distance)
        self._lock_piece()
        return distance * SCORE_HARD_DROP

    def rotate_clockwise(self) -> bool:
        """
        Attempt to rotate the current piece clockwise.

        Returns:
            True if rotation was successful, False otherwise
        """
        if not self.current_piece or self.game_over or self.paused:
            return False

        self.current_piece.rotate_clockwise()
        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.rotate_counterclockwise()  # Undo rotation
            return False
        return True

    def rotate_counterclockwise(self) -> bool:
        """
        Attempt to rotate the current piece counterclockwise.

        Returns:
            True if rotation was successful, False otherwise
        """
        if not self.current_piece or self.game_over or self.paused:
            return False

        self.current_piece.rotate_counterclockwise()
        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.rotate_clockwise()  # Undo rotation
            return False
        return True

    def _lock_piece(self) -> None:
        """Lock the current piece and handle line clearing."""
        if not self.current_piece:
            return

        self.board.lock_tetromino(self.current_piece)
        lines = self.board.clear_lines()

        if lines > 0:
            self._update_score(lines)
            self.lines_cleared += lines
            self._update_level()

        # Check for game over before spawning new piece
        if self.board.is_game_over():
            self.game_over = True
        else:
            self._spawn_new_piece()

    def _update_score(self, lines: int) -> None:
        """
        Update score based on lines cleared.

        Args:
            lines: Number of lines cleared
        """
        base_score = {
            1: SCORE_SINGLE_LINE,
            2: SCORE_DOUBLE_LINE,
            3: SCORE_TRIPLE_LINE,
            4: SCORE_TETRIS,
        }.get(lines, 0)

        self.score += base_score * self.level

    def _update_level(self) -> None:
        """Update level based on lines cleared."""
        new_level = (self.lines_cleared // LINES_PER_LEVEL) + 1
        if new_level > self.level:
            self.level = new_level

    def get_fall_speed(self) -> int:
        """
        Get current fall speed in milliseconds.

        Returns:
            Time in milliseconds between automatic falls
        """
        speed = INITIAL_FALL_SPEED - (self.level - 1) * FALL_SPEED_DECREASE
        return max(speed, MIN_FALL_SPEED)

    def toggle_pause(self) -> None:
        """Toggle pause state."""
        if not self.game_over:
            self.paused = not self.paused

    def reset(self) -> None:
        """Reset the game to initial state."""
        self.board.reset()
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self._spawn_new_piece()
        self.next_piece = Tetromino.create_random()

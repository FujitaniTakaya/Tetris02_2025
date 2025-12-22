"""
Renderer class for drawing the game.
Separates rendering logic from game logic (View in MVC).
"""

import pygame
from typing import Optional
from tetris.models.game import Game
from tetris.models.tetromino import Tetromino
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE, GRID_WIDTH, GRID_HEIGHT,
    BOARD_X, BOARD_Y, COLOR_BLACK, COLOR_WHITE, COLOR_GRAY,
    COLOR_DARK_GRAY, COLOR_LIGHT_GRAY, INFO_PANEL_X, INFO_PANEL_Y,
    FONT_SIZE_LARGE, FONT_SIZE_MEDIUM, FONT_SIZE_SMALL, GAME_TITLE
)


class Renderer:
    """
    Handles all rendering operations.
    Responsible only for drawing - no game logic here.
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initialize the renderer.

        Args:
            screen: Pygame surface to render to
        """
        self.screen = screen

        # Initialize fonts
        pygame.font.init()
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)

    def render(self, game: Game) -> None:
        """
        Render the entire game state.

        Args:
            game: The game instance to render
        """
        self.screen.fill(COLOR_BLACK)

        self._draw_board(game)
        self._draw_current_piece(game)
        self._draw_ghost_piece(game)
        self._draw_grid()
        self._draw_info_panel(game)

        if game.paused:
            self._draw_pause_overlay()
        elif game.game_over:
            self._draw_game_over_overlay()

        pygame.display.flip()

    def _draw_board(self, game: Game) -> None:
        """
        Draw the locked blocks on the board.

        Args:
            game: The game instance
        """
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = game.board.get_cell(x, y)
                if color:
                    self._draw_block(x, y, color)

    def _draw_current_piece(self, game: Game) -> None:
        """
        Draw the current falling piece.

        Args:
            game: The game instance
        """
        if not game.current_piece:
            return

        for x, y in game.current_piece.get_blocks():
            self._draw_block(x, y, game.current_piece.color)

    def _draw_ghost_piece(self, game: Game) -> None:
        """
        Draw a ghost piece showing where the current piece will land.

        Args:
            game: The game instance
        """
        if not game.current_piece or game.game_over:
            return

        # Calculate drop position
        distance = game.board.get_drop_distance(game.current_piece)
        if distance == 0:
            return

        # Draw ghost blocks (semi-transparent)
        for x, y in game.current_piece.get_blocks():
            ghost_y = y + distance
            self._draw_ghost_block(x, ghost_y, game.current_piece.color)

    def _draw_block(self, grid_x: int, grid_y: int, color: tuple) -> None:
        """
        Draw a single block.

        Args:
            grid_x: Grid x position
            grid_y: Grid y position
            color: Block color (R, G, B)
        """
        x = BOARD_X + grid_x * BLOCK_SIZE
        y = BOARD_Y + grid_y * BLOCK_SIZE

        # Draw filled rectangle
        pygame.draw.rect(self.screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

        # Draw border for 3D effect
        pygame.draw.rect(self.screen, COLOR_LIGHT_GRAY,
                        (x, y, BLOCK_SIZE, BLOCK_SIZE), 1)

    def _draw_ghost_block(self, grid_x: int, grid_y: int, color: tuple) -> None:
        """
        Draw a ghost block (semi-transparent outline).

        Args:
            grid_x: Grid x position
            grid_y: Grid y position
            color: Block color (R, G, B)
        """
        x = BOARD_X + grid_x * BLOCK_SIZE
        y = BOARD_Y + grid_y * BLOCK_SIZE

        # Draw outline only
        pygame.draw.rect(self.screen, color,
                        (x, y, BLOCK_SIZE, BLOCK_SIZE), 2)

    def _draw_grid(self) -> None:
        """Draw the grid lines."""
        # Draw vertical lines
        for x in range(GRID_WIDTH + 1):
            start_x = BOARD_X + x * BLOCK_SIZE
            pygame.draw.line(self.screen, COLOR_DARK_GRAY,
                           (start_x, BOARD_Y),
                           (start_x, BOARD_Y + GRID_HEIGHT * BLOCK_SIZE))

        # Draw horizontal lines
        for y in range(GRID_HEIGHT + 1):
            start_y = BOARD_Y + y * BLOCK_SIZE
            pygame.draw.line(self.screen, COLOR_DARK_GRAY,
                           (BOARD_X, start_y),
                           (BOARD_X + GRID_WIDTH * BLOCK_SIZE, start_y))

        # Draw board border
        pygame.draw.rect(self.screen, COLOR_WHITE,
                        (BOARD_X - 2, BOARD_Y - 2,
                         GRID_WIDTH * BLOCK_SIZE + 4,
                         GRID_HEIGHT * BLOCK_SIZE + 4), 2)

    def _draw_info_panel(self, game: Game) -> None:
        """
        Draw the information panel (score, level, next piece).

        Args:
            game: The game instance
        """
        y_offset = INFO_PANEL_Y

        # Score
        self._draw_text("SCORE", INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 30
        self._draw_text(str(game.score), INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 50

        # Level
        self._draw_text("LEVEL", INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 30
        self._draw_text(str(game.level), INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 50

        # Lines
        self._draw_text("LINES", INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 30
        self._draw_text(str(game.lines_cleared), INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 60

        # Next piece
        self._draw_text("NEXT", INFO_PANEL_X, y_offset,
                       self.font_medium, COLOR_WHITE)
        y_offset += 40
        self._draw_next_piece(game.next_piece, INFO_PANEL_X, y_offset)

        # Controls (at bottom)
        y_offset = WINDOW_HEIGHT - 200
        self._draw_text("CONTROLS", INFO_PANEL_X, y_offset,
                       self.font_small, COLOR_GRAY)
        y_offset += 25
        controls = [
            "← → : Move",
            "↓ : Soft Drop",
            "↑/Z : Rotate",
            "Space : Hard Drop",
            "P : Pause",
            "R : Restart",
            "ESC : Quit"
        ]
        for control in controls:
            self._draw_text(control, INFO_PANEL_X, y_offset,
                          self.font_small, COLOR_GRAY)
            y_offset += 20

    def _draw_next_piece(self, piece: Optional[Tetromino], x: int, y: int) -> None:
        """
        Draw the next piece preview.

        Args:
            piece: The next tetromino to display
            x: X position for preview
            y: Y position for preview
        """
        if not piece:
            return

        # Draw a small preview box
        preview_size = 4 * BLOCK_SIZE
        pygame.draw.rect(self.screen, COLOR_DARK_GRAY,
                        (x, y, preview_size, preview_size))
        pygame.draw.rect(self.screen, COLOR_WHITE,
                        (x, y, preview_size, preview_size), 1)

        # Center the piece in the preview box
        preview_piece = piece.copy()
        preview_piece.x = 0
        preview_piece.y = 0

        # Calculate center offset
        blocks = preview_piece.get_blocks()
        min_x = min(bx for bx, _ in blocks)
        max_x = max(bx for bx, _ in blocks)
        min_y = min(by for _, by in blocks)
        max_y = max(by for _, by in blocks)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        offset_x = (4 - width) // 2 - min_x
        offset_y = (4 - height) // 2 - min_y

        # Draw blocks
        for bx, by in blocks:
            block_x = x + (bx + offset_x) * (BLOCK_SIZE // 2) + BLOCK_SIZE // 4
            block_y = y + (by + offset_y) * (BLOCK_SIZE // 2) + BLOCK_SIZE // 4
            pygame.draw.rect(self.screen, piece.color,
                           (block_x, block_y, BLOCK_SIZE // 2, BLOCK_SIZE // 2))

    def _draw_pause_overlay(self) -> None:
        """Draw the pause overlay."""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(COLOR_BLACK)
        self.screen.blit(overlay, (0, 0))

        self._draw_centered_text("PAUSED", WINDOW_HEIGHT // 2 - 50,
                                self.font_large, COLOR_WHITE)
        self._draw_centered_text("Press P to resume", WINDOW_HEIGHT // 2 + 20,
                                self.font_medium, COLOR_GRAY)

    def _draw_game_over_overlay(self) -> None:
        """Draw the game over overlay."""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(COLOR_BLACK)
        self.screen.blit(overlay, (0, 0))

        self._draw_centered_text("GAME OVER", WINDOW_HEIGHT // 2 - 50,
                                self.font_large, COLOR_WHITE)
        self._draw_centered_text("Press R to restart", WINDOW_HEIGHT // 2 + 20,
                                self.font_medium, COLOR_GRAY)

    def _draw_text(self, text: str, x: int, y: int,
                   font: pygame.font.Font, color: tuple) -> None:
        """
        Draw text at specified position.

        Args:
            text: Text to draw
            x: X position
            y: Y position
            font: Font to use
            color: Text color
        """
        surface = font.render(text, True, color)
        self.screen.blit(surface, (x, y))

    def _draw_centered_text(self, text: str, y: int,
                           font: pygame.font.Font, color: tuple) -> None:
        """
        Draw centered text.

        Args:
            text: Text to draw
            y: Y position
            font: Font to use
            color: Text color
        """
        surface = font.render(text, True, color)
        x = (WINDOW_WIDTH - surface.get_width()) // 2
        self.screen.blit(surface, (x, y))

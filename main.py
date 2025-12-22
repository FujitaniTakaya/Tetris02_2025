"""
Main entry point for Tetris game.
Initializes pygame and runs the game loop.
"""

import pygame
import sys
from tetris.models.game import Game
from tetris.views.renderer import Renderer
from tetris.controllers.input_handler import InputHandler
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, GAME_TITLE


class TetrisApp:
    """
    Main application class.
    Coordinates the Model-View-Controller components.
    """

    def __init__(self):
        """Initialize the application."""
        # Initialize pygame
        pygame.init()

        # Create window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        # Create MVC components
        self.game = Game()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()

        # Game loop timing
        self.clock = pygame.time.Clock()
        self.last_fall_time = 0

    def run(self) -> None:
        """Run the main game loop."""
        running = True

        while running:
            current_time = pygame.time.get_ticks()

            # Handle input
            running = self.input_handler.handle_events(self.game)

            # Update game state (automatic falling)
            if not self.game.paused and not self.game.game_over:
                fall_speed = self.game.get_fall_speed()
                if current_time - self.last_fall_time >= fall_speed:
                    self.game.move_down()
                    self.last_fall_time = current_time

            # Render
            self.renderer.render(self.game)

            # Maintain framerate
            self.clock.tick(FPS)

        self.quit()

    def quit(self) -> None:
        """Clean up and exit."""
        pygame.quit()
        sys.exit()


def main():
    """Main function."""
    app = TetrisApp()
    app.run()


if __name__ == "__main__":
    main()

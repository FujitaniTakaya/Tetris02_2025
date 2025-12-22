"""
Input handler for processing user input.
Separates input handling from game logic (Controller in MVC).
"""

import pygame
from tetris.models.game import Game


class InputHandler:
    """
    Handles keyboard input and translates it to game actions.
    Responsible only for input - no game logic here.
    """

    def __init__(self):
        """Initialize the input handler."""
        self.key_repeat_delay = 150  # Milliseconds before key repeat starts
        self.key_repeat_interval = 50  # Milliseconds between repeats
        self.last_move_time = {
            'left': 0,
            'right': 0,
            'down': 0,
        }

    def handle_events(self, game: Game) -> bool:
        """
        Process pygame events and update game state.

        Args:
            game: The game instance to control

        Returns:
            False if user wants to quit, True otherwise
        """
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if not self._handle_keydown(event.key, game):
                    return False

        # Handle continuous key press for movement
        self._handle_continuous_input(game, current_time)

        return True

    def _handle_keydown(self, key: int, game: Game) -> bool:
        """
        Handle key press events.

        Args:
            key: The key that was pressed
            game: The game instance

        Returns:
            False if user wants to quit, True otherwise
        """
        # Quit
        if key == pygame.K_ESCAPE:
            return False

        # Pause
        if key == pygame.K_p:
            game.toggle_pause()
            return True

        # Restart
        if key == pygame.K_r:
            game.reset()
            return True

        # Don't process game controls if paused or game over
        if game.paused or game.game_over:
            return True

        # Rotation
        if key in (pygame.K_UP, pygame.K_z):
            game.rotate_counterclockwise()
        elif key in (pygame.K_x, pygame.K_LSHIFT, pygame.K_RSHIFT):
            game.rotate_clockwise()

        # Hard drop
        elif key == pygame.K_SPACE:
            points = game.hard_drop()
            game.score += points

        # Movement (handled in continuous input for smooth movement)
        elif key == pygame.K_LEFT:
            game.move_left()
            self.last_move_time['left'] = pygame.time.get_ticks()
        elif key == pygame.K_RIGHT:
            game.move_right()
            self.last_move_time['right'] = pygame.time.get_ticks()
        elif key == pygame.K_DOWN:
            game.soft_drop()
            self.last_move_time['down'] = pygame.time.get_ticks()

        return True

    def _handle_continuous_input(self, game: Game, current_time: int) -> None:
        """
        Handle continuous key presses for smooth movement.

        Args:
            game: The game instance
            current_time: Current time in milliseconds
        """
        if game.paused or game.game_over:
            return

        keys = pygame.key.get_pressed()

        # Left movement
        if keys[pygame.K_LEFT]:
            if current_time - self.last_move_time['left'] >= self.key_repeat_interval:
                if game.move_left():
                    self.last_move_time['left'] = current_time

        # Right movement
        if keys[pygame.K_RIGHT]:
            if current_time - self.last_move_time['right'] >= self.key_repeat_interval:
                if game.move_right():
                    self.last_move_time['right'] = current_time

        # Down movement (soft drop)
        if keys[pygame.K_DOWN]:
            if current_time - self.last_move_time['down'] >= self.key_repeat_interval:
                points = game.soft_drop()
                game.score += points
                self.last_move_time['down'] = current_time

"""
Game configuration and constants.
All magic numbers are defined here for easy maintenance.
"""

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
GAME_TITLE = "Tetris 2025 - Code Quality Edition"

# Grid settings
GRID_WIDTH = 10  # Number of columns
GRID_HEIGHT = 20  # Number of rows
BLOCK_SIZE = 25  # Size of each block in pixels

# Calculate board position (centered)
BOARD_X = (WINDOW_WIDTH - GRID_WIDTH * BLOCK_SIZE) // 2 - 100
BOARD_Y = (WINDOW_HEIGHT - GRID_HEIGHT * BLOCK_SIZE) // 2

# Colors (RGB)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_GRAY = (40, 40, 40)
COLOR_LIGHT_GRAY = (200, 200, 200)

# Tetromino colors
COLOR_CYAN = (0, 255, 255)      # I piece
COLOR_YELLOW = (255, 255, 0)    # O piece
COLOR_PURPLE = (128, 0, 128)    # T piece
COLOR_GREEN = (0, 255, 0)       # S piece
COLOR_RED = (255, 0, 0)         # Z piece
COLOR_BLUE = (0, 0, 255)        # J piece
COLOR_ORANGE = (255, 165, 0)    # L piece

# Game mechanics
INITIAL_FALL_SPEED = 1000  # Milliseconds between automatic falls
FALL_SPEED_DECREASE = 50   # Speed increase per level (ms faster)
MIN_FALL_SPEED = 100       # Minimum fall speed (fastest)
SOFT_DROP_SPEED = 50       # Speed when holding down arrow
LOCK_DELAY = 500           # Milliseconds before piece locks after landing

# Scoring
SCORE_SINGLE_LINE = 100
SCORE_DOUBLE_LINE = 300
SCORE_TRIPLE_LINE = 500
SCORE_TETRIS = 800  # Four lines at once
SCORE_SOFT_DROP = 1  # Per cell
SCORE_HARD_DROP = 2  # Per cell

# Level progression
LINES_PER_LEVEL = 10  # Lines needed to advance one level

# UI settings
SIDEBAR_WIDTH = 200
INFO_PANEL_X = BOARD_X + GRID_WIDTH * BLOCK_SIZE + 30
INFO_PANEL_Y = BOARD_Y
FONT_SIZE_LARGE = 32
FONT_SIZE_MEDIUM = 24
FONT_SIZE_SMALL = 18

# Tetromino shapes
# Each shape is defined as a list of rotations
# Each rotation is a list of (x, y) offsets from the center
TETROMINO_SHAPES = {
    'I': [
        [(0, 0), (-1, 0), (1, 0), (2, 0)],   # Horizontal
        [(0, 0), (0, -1), (0, 1), (0, 2)],   # Vertical
        [(0, 0), (-1, 0), (1, 0), (2, 0)],   # Horizontal
        [(0, 0), (0, -1), (0, 1), (0, 2)],   # Vertical
    ],
    'O': [
        [(0, 0), (1, 0), (0, 1), (1, 1)],    # All rotations are the same
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ],
    'T': [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],   # T pointing up
        [(0, 0), (0, -1), (0, 1), (-1, 0)],  # T pointing right
        [(0, 0), (-1, 0), (1, 0), (0, -1)],  # T pointing down
        [(0, 0), (0, -1), (0, 1), (1, 0)],   # T pointing left
    ],
    'S': [
        [(0, 0), (-1, 0), (0, 1), (1, 1)],   # Horizontal
        [(0, 0), (0, -1), (1, 0), (1, 1)],   # Vertical
        [(0, 0), (-1, 0), (0, 1), (1, 1)],   # Horizontal
        [(0, 0), (0, -1), (1, 0), (1, 1)],   # Vertical
    ],
    'Z': [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],   # Horizontal
        [(0, 0), (0, 1), (1, 0), (1, -1)],   # Vertical
        [(0, 0), (1, 0), (0, 1), (-1, 1)],   # Horizontal
        [(0, 0), (0, 1), (1, 0), (1, -1)],   # Vertical
    ],
    'J': [
        [(0, 0), (-1, 0), (1, 0), (-1, 1)],  # J base down
        [(0, 0), (0, -1), (0, 1), (1, 1)],   # J base right
        [(0, 0), (-1, 0), (1, 0), (1, -1)],  # J base up
        [(0, 0), (0, -1), (0, 1), (-1, -1)], # J base left
    ],
    'L': [
        [(0, 0), (-1, 0), (1, 0), (1, 1)],   # L base down
        [(0, 0), (0, -1), (0, 1), (1, -1)],  # L base right
        [(0, 0), (-1, 0), (1, 0), (-1, -1)], # L base up
        [(0, 0), (0, -1), (0, 1), (-1, 1)],  # L base left
    ],
}

# Map tetromino types to colors
TETROMINO_COLORS = {
    'I': COLOR_CYAN,
    'O': COLOR_YELLOW,
    'T': COLOR_PURPLE,
    'S': COLOR_GREEN,
    'Z': COLOR_RED,
    'J': COLOR_BLUE,
    'L': COLOR_ORANGE,
}

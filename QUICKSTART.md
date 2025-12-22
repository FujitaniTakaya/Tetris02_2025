# Quick Start Guide

## Installation

1. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - Requires Python 3.8 or higher

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   This installs Pygame 2.5.2

3. **Run the game**
   ```bash
   python main.py
   ```

## Game Screenshot (ASCII Representation)

```
╔══════════════════════════════════════════════════════════════════╗
║                  TETRIS 2025 - Code Quality Edition              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌────────────────────┐                                          ║
║  │                    │        SCORE                             ║
║  │                    │        1500                              ║
║  │                    │                                          ║
║  │                    │        LEVEL                             ║
║  │        ██          │        3                                 ║
║  │        ██          │                                          ║
║  │      ██████        │        LINES                             ║
║  │                    │        25                                ║
║  │                    │                                          ║
║  │                    │        NEXT                              ║
║  │      ┌ ─┐          │        ┌────┐                            ║
║  │      │  │          │        │ ██ │                            ║
║  │      │  │          │        │ ██ │                            ║
║  │      │  │          │        └────┘                            ║
║  │      │  │          │                                          ║
║  │      └ ─┘          │        CONTROLS                          ║
║  │        ▼           │        ← → : Move                        ║
║  │      ██████        │        ↓ : Soft Drop                     ║
║  │      ██████        │        ↑/Z : Rotate CCW                  ║
║  │    ████████████    │        X : Rotate CW                     ║
║  │  ██████████████    │        Space : Hard Drop                 ║
║  └────────────────────┘        P : Pause                         ║
║                                 R : Restart                       ║
║                                 ESC : Quit                        ║
╚══════════════════════════════════════════════════════════════════╝
```

## Features Explained

### 1. **Ghost Piece** (dotted outline)
- Shows where the current piece will land
- Helps plan placement more effectively

### 2. **Next Piece Preview**
- Small box showing the next piece
- Allows strategic planning

### 3. **Score System**
- Single line: 100 points × level
- Double line: 300 points × level
- Triple line: 500 points × level
- Tetris (4 lines): 800 points × level
- Soft drop: 1 point per cell
- Hard drop: 2 points per cell

### 4. **Level Progression**
- Advances every 10 lines cleared
- Speed increases with each level
- No maximum level

### 5. **Smooth Controls**
- Responsive key repeat
- Separate timings for different actions
- Professional game feel

## Control Details

### Movement Controls
- **Left Arrow (←)**: Move piece left
- **Right Arrow (→)**: Move piece right
- **Down Arrow (↓)**: Soft drop (speeds up falling, earns points)

### Rotation Controls
- **Up Arrow (↑) or Z**: Rotate counterclockwise (90° left)
- **X or Shift**: Rotate clockwise (90° right)

### Special Actions
- **Spacebar**: Hard drop (instant drop to bottom, earns more points)

### Game Controls
- **P**: Pause/unpause the game
- **R**: Restart the game (anytime)
- **ESC**: Quit the game

## Gameplay Tips

1. **Use the ghost piece**: It shows exactly where your piece will land
2. **Plan ahead**: Look at the next piece to strategize
3. **Build flat**: Try to keep the surface level
4. **Don't rush**: Take time to position pieces correctly
5. **Clear lines**: Focus on clearing lines rather than just surviving
6. **Tetris bonus**: Clearing 4 lines at once gives the most points

## Code Structure (For Developers)

```
main.py → TetrisApp
    ├─→ Game (Model)
    │   ├─→ Board (collision, line clearing)
    │   └─→ Tetromino (pieces)
    │
    ├─→ Renderer (View)
    │   └─→ Draws everything on screen
    │
    └─→ InputHandler (Controller)
        └─→ Processes keyboard input
```

## Testing

Run the test suite to verify game logic:
```bash
python test_game.py
```

Expected output:
```
✓ Game initialization test passed
✓ Tetromino test passed
✓ Board test passed
✓ Game mechanics test passed
✓ Line clearing test passed
✓ Collision detection test passed

ALL TESTS PASSED! ✓
```

## Troubleshooting

### "pygame not found"
```bash
pip install pygame
```

### "ModuleNotFoundError: No module named 'tetris'"
Make sure you're running from the project root directory:
```bash
cd /path/to/Tetris02_2025
python main.py
```

### Game runs too fast/slow
Adjust `FPS` in `config.py` (default: 60)

### Want to change difficulty
Adjust these constants in `config.py`:
- `INITIAL_FALL_SPEED`: Starting speed (default: 1000ms)
- `FALL_SPEED_DECREASE`: Speed increase per level (default: 50ms)
- `LINES_PER_LEVEL`: Lines needed per level (default: 10)

## Customization

All game parameters are in `config.py`:
- Window size
- Grid dimensions
- Colors
- Scoring values
- Speed settings
- Piece shapes

Example: To make the game easier, increase `INITIAL_FALL_SPEED` to 1500.

## Enjoy the Game! 🎮

This implementation focuses on clean, maintainable code while providing a complete and enjoyable Tetris experience.

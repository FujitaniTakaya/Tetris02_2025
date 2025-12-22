# Tetris02_2025

自作テトリス二作目です。
主に前回のもののコード方面の向上が目的です。

## Improvements from Tetris01_2025

### Code Quality Enhancements
1. **Clean Architecture**: Implemented Model-View-Controller (MVC) pattern
2. **No Global Variables**: All state is properly encapsulated in classes
3. **Named Constants**: Replaced all magic numbers with well-named constants
4. **Separation of Concerns**: Game logic, rendering, and input handling are separated
5. **Cross-Platform**: Uses Python and Pygame for better portability
6. **Memory Safety**: Automatic memory management with Python
7. **Maintainability**: Clear module structure and documentation

### Project Structure
```
tetris/
├── config.py          # Game configuration and constants
├── models/
│   ├── __init__.py
│   ├── tetromino.py   # Tetromino (piece) definitions and logic
│   ├── board.py       # Game board and collision detection
│   └── game.py        # Core game state and logic
├── views/
│   ├── __init__.py
│   └── renderer.py    # Graphics rendering
└── controllers/
    ├── __init__.py
    └── input_handler.py  # Input handling
main.py                # Entry point
```

## Requirements
- Python 3.8 or higher
- Pygame 2.5.2 or higher

## Installation
```bash
pip install -r requirements.txt
```

## How to Play
```bash
python main.py
```

### Controls
- **←/→**: Move piece left/right
- **↓**: Soft drop (move down faster)
- **↑ or Z**: Rotate counterclockwise
- **X or Shift**: Rotate clockwise
- **Space**: Hard drop (instant drop)
- **P**: Pause game
- **ESC**: Quit game

## Features
- Classic Tetris gameplay
- Score tracking
- Level progression (increasing speed)
- Line clearing with animations
- Next piece preview
- Clean, readable code structure
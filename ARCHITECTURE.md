# Architecture Overview

## MVC Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         MAIN.PY                                  │
│                     (Application Entry)                          │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    TetrisApp                              │  │
│  │  - Initializes pygame                                     │  │
│  │  - Creates MVC components                                 │  │
│  │  - Runs main game loop                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            │ coordinates
                            ▼
        ┌───────────────────┴───────────────────┐
        │                                       │
        ▼                                       ▼
┌───────────────┐                      ┌───────────────┐
│  CONTROLLER   │                      │     VIEW      │
│               │                      │               │
│ InputHandler  │                      │   Renderer    │
│               │                      │               │
│ - Processes   │                      │ - Draws board │
│   keyboard    │                      │ - Draws       │
│   events      │                      │   pieces      │
│ - Translates  │                      │ - Draws UI    │
│   to game     │                      │ - Shows       │
│   actions     │                      │   overlays    │
│               │                      │               │
└───────┬───────┘                      └───────▲───────┘
        │                                      │
        │ updates                              │ reads
        │                                      │
        ▼                                      │
┌─────────────────────────────────────────────┴───────┐
│                      MODEL                          │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │                 Game                         │  │
│  │  - Core game state                           │  │
│  │  - Score, level, lines                       │  │
│  │  - Current & next pieces                     │  │
│  │  - Game over & pause state                   │  │
│  │  - Implements game rules                     │  │
│  └────────┬───────────────────┬─────────────────┘  │
│           │ contains          │ contains            │
│           ▼                   ▼                     │
│  ┌──────────────┐    ┌──────────────────┐          │
│  │    Board     │    │    Tetromino     │          │
│  │              │    │                  │          │
│  │ - Grid state │    │ - Shape type     │          │
│  │ - Collision  │    │ - Position       │          │
│  │   detection  │    │ - Rotation       │          │
│  │ - Line clear │    │ - Color          │          │
│  └──────────────┘    └──────────────────┘          │
│                                                      │
└──────────────────────────────────────────────────────┘

                            ▲
                            │
                    uses constants from
                            │
                    ┌───────┴────────┐
                    │   CONFIG.PY    │
                    │                │
                    │ - Window size  │
                    │ - Grid size    │
                    │ - Colors       │
                    │ - Shapes       │
                    │ - Scoring      │
                    │ - All constants│
                    └────────────────┘
```

## Data Flow

```
User Input → InputHandler → Game (Model) → Renderer (View) → Screen
     ▲                          │              │
     │                          │              │
     └──────────────────────────┴──────────────┘
                    Game Loop (60 FPS)
```

## Component Responsibilities

### Model (Business Logic)
- **Game**: Manages game state and rules
  - Piece spawning
  - Movement validation
  - Scoring calculation
  - Level progression
  - Game over detection

- **Board**: Manages playfield
  - Grid state (locked blocks)
  - Collision detection
  - Line clearing
  - Position validation

- **Tetromino**: Represents game pieces
  - Shape definitions
  - Rotation logic
  - Position tracking
  - Block calculations

### View (Presentation)
- **Renderer**: Handles all drawing
  - Board rendering
  - Piece rendering
  - Ghost piece preview
  - UI elements (score, level, next piece)
  - Overlays (pause, game over)

### Controller (Input)
- **InputHandler**: Processes user input
  - Keyboard event handling
  - Key repeat for smooth movement
  - Action mapping (keys to game actions)

### Configuration
- **config.py**: Centralized constants
  - All magic numbers eliminated
  - Easy to adjust game parameters
  - Single source of truth

## Key Design Principles Applied

1. **Separation of Concerns**
   - Each component has one clear responsibility
   - Changes in one area don't affect others

2. **Encapsulation**
   - All state is private to classes
   - Public interfaces are well-defined
   - No global mutable state

3. **Single Responsibility Principle**
   - Each class does one thing well
   - Easy to understand and maintain

4. **Open/Closed Principle**
   - Easy to extend (add new features)
   - No need to modify existing code

5. **Dependency Inversion**
   - High-level modules don't depend on low-level details
   - All depend on abstractions (interfaces)

## Benefits of This Architecture

✓ **Testable**: Each component can be tested independently
✓ **Maintainable**: Changes are localized and predictable
✓ **Readable**: Clear structure, easy to navigate
✓ **Extensible**: New features fit naturally into the structure
✓ **Debuggable**: Clear data flow makes bugs easy to find
✓ **Reusable**: Components can be used in other projects
✓ **Documented**: Every class and method is well-documented

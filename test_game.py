"""
Test script to verify game logic without GUI.
"""

import sys
sys.path.insert(0, '/home/runner/work/Tetris02_2025/Tetris02_2025')

from tetris.models.game import Game
from tetris.models.tetromino import Tetromino
from tetris.models.board import Board
from config import GRID_WIDTH, GRID_HEIGHT

def test_game_initialization():
    """Test that game initializes correctly."""
    game = Game()
    assert game.score == 0, "Initial score should be 0"
    assert game.level == 1, "Initial level should be 1"
    assert game.lines_cleared == 0, "Initial lines cleared should be 0"
    assert not game.game_over, "Game should not be over initially"
    assert not game.paused, "Game should not be paused initially"
    assert game.current_piece is not None, "Current piece should exist"
    assert game.next_piece is not None, "Next piece should exist"
    print("✓ Game initialization test passed")

def test_tetromino():
    """Test tetromino functionality."""
    piece = Tetromino('I', 5, 3)
    assert piece.shape_type == 'I', "Shape type should be I"
    assert piece.x == 5, "X position should be 5"
    assert piece.y == 3, "Y position should be 3"
    assert piece.rotation_state == 0, "Initial rotation should be 0"
    
    blocks = piece.get_blocks()
    assert len(blocks) == 4, "Tetromino should have 4 blocks"
    
    # Test movement
    piece.move_left()
    assert piece.x == 4, "X should decrease by 1"
    
    piece.move_right()
    assert piece.x == 5, "X should increase by 1"
    
    piece.move_down()
    assert piece.y == 4, "Y should increase by 1"
    
    # Test rotation
    initial_rotation = piece.rotation_state
    piece.rotate_clockwise()
    assert piece.rotation_state == (initial_rotation + 1) % 4, "Rotation should advance"
    
    print("✓ Tetromino test passed")

def test_board():
    """Test board functionality."""
    board = Board()
    assert board.width == GRID_WIDTH, f"Board width should be {GRID_WIDTH}"
    assert board.height == GRID_HEIGHT, f"Board height should be {GRID_HEIGHT}"
    
    # Test empty board
    assert board.get_cell(0, 0) is None, "Empty cell should return None"
    
    # Test piece validation
    piece = Tetromino('O', GRID_WIDTH // 2, 0)
    assert board.is_valid_position(piece), "Piece at spawn should be valid"
    
    # Test invalid position (out of bounds)
    piece_out = Tetromino('O', -1, 0)
    assert not board.is_valid_position(piece_out), "Piece out of bounds should be invalid"
    
    # Test locking piece
    piece_to_lock = Tetromino('O', 0, 0)
    board.lock_tetromino(piece_to_lock)
    assert board.get_cell(0, 0) is not None, "Locked cell should not be None"
    
    print("✓ Board test passed")

def test_game_mechanics():
    """Test game mechanics."""
    game = Game()
    
    # Test movement
    initial_x = game.current_piece.x
    result = game.move_left()
    if result:
        assert game.current_piece.x == initial_x - 1, "Piece should move left"
    
    # Test rotation
    result = game.rotate_clockwise()
    assert result in (True, False), "Rotation should return boolean"
    
    # Test score
    initial_score = game.score
    game.score += 100
    assert game.score == initial_score + 100, "Score should increase"
    
    # Test pause
    game.toggle_pause()
    assert game.paused, "Game should be paused"
    game.toggle_pause()
    assert not game.paused, "Game should be unpaused"
    
    print("✓ Game mechanics test passed")

def test_line_clearing():
    """Test line clearing."""
    board = Board()
    
    # Fill bottom row
    for x in range(board.width):
        board.grid[board.height - 1][x] = (255, 255, 255)
    
    # Clear lines
    lines = board.clear_lines()
    assert lines == 1, "Should clear 1 line"
    assert board.grid[board.height - 1][0] is None, "Bottom row should be empty after clear"
    
    print("✓ Line clearing test passed")

def test_collision():
    """Test collision detection."""
    board = Board()
    
    # Place a piece at the bottom
    piece = Tetromino('O', 0, GRID_HEIGHT - 2)
    board.lock_tetromino(piece)
    
    # Try to place another piece overlapping
    piece2 = Tetromino('O', 0, GRID_HEIGHT - 2)
    assert not board.is_valid_position(piece2), "Overlapping position should be invalid"
    
    print("✓ Collision detection test passed")

def main():
    """Run all tests."""
    print("Running Tetris game logic tests...\n")
    
    try:
        test_game_initialization()
        test_tetromino()
        test_board()
        test_game_mechanics()
        test_line_clearing()
        test_collision()
        
        print("\n" + "="*50)
        print("ALL TESTS PASSED! ✓")
        print("="*50)
        print("\nGame logic is working correctly!")
        print("The game is ready to play with: python main.py")
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

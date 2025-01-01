import cv2 as opencv
import numpy
from setting import *

# Ball and Paddle Initialization
ball_pos = [screen_width // 2, screen_height // 2]
ball_velocity = [ball_speed, ball_speed]

player_pos = screen_height // 2 - paddle_height // 2
enemy_pos = screen_height // 2 - paddle_height // 2

def init_game():
    """Initializes the game window and other settings."""
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)

def update_game(key):
    """Updates the game state based on player input."""
    global player_pos, enemy_pos

    if key == UP_KEY and player_pos > 0:
        player_pos -= player_speed
    if key == DOWN_KEY and player_pos < screen_height - paddle_height:
        player_pos += player_speed

def draw_game():
    """Draws the current game state on the screen."""
    # Create scene background
    scene = numpy.full((screen_height, screen_width, 3), Mint, dtype=numpy.uint8)
    
    # Draw line
    opencv.line(scene, (screen_width // 2, 0), (screen_width // 2, screen_height), Snow, 2)
    
    # Draw paddles
    opencv.rectangle(scene, (screen_width - paddle_margin - paddle_width, player_pos),
                     (screen_width - paddle_margin, player_pos + paddle_height), Snow, -1)
    opencv.rectangle(scene, (paddle_margin, enemy_pos),
                     (paddle_margin + paddle_width, enemy_pos + paddle_height), Snow, -1)

    # Draw ball
    opencv.circle(scene, tuple(ball_pos), ball_size, Gold, -1)

    # Display scores
    font = opencv.FONT_HERSHEY_SIMPLEX
    opencv.putText(scene, "0", (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, Snow, 2)
    opencv.putText(scene, "0", (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, Snow, 2)

    return scene

def main():
    """Main game loop."""
    init_game()

    while True:
        key = opencv.waitKey(1) & 0xFF

        # Update game state
        update_game(key)

        # Draw the game
        scene = draw_game()

        # Exit condition
        if key == ESC_KEY:
            break

        # Display the game
        opencv.imshow(game_name, scene)

    opencv.destroyAllWindows()

if __name__ == "__main__":
    main()

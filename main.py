import cv2 as opencv
import numpy
from setting import *
from paddle import Paddle
from ball import Ball

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player_paddle = Paddle(screen_width - paddle_margin - paddle_width, 
                       screen_height, paddle_width, paddle_height, 
                       player_speed, paddle_margin)
enemy_paddle = Paddle(paddle_margin, 
                      screen_height, paddle_width, paddle_height, 
                      player_speed, paddle_margin)

def init_game():
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)

def update_game(key):
    player_paddle.move(key)

def draw_game():
    # Create scene background
    scene = numpy.full((screen_height, screen_width, 3), MINT, dtype=numpy.uint8)
    
    # Draw center line
    opencv.line(scene, (screen_width // 2, 0), (screen_width // 2, screen_height), SNOW, 2)
    
    # Draw paddles
    player_paddle.draw(scene, SNOW)
    enemy_paddle.draw(scene, SNOW)

    # Draw ball
    ball.draw(scene)

    # Display scores
    font = opencv.FONT_HERSHEY_SIMPLEX
    opencv.putText(scene, "0", (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)
    opencv.putText(scene, "0", (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)

    return scene

def main():
    init_game()

    while True:
        key = opencv.waitKey(delay) & KEY_MASK

        update_game(key)
        scene = draw_game()

        if key == KEY_ESC:
            break

        opencv.imshow(game_name, scene)

    opencv.destroyAllWindows()

if __name__ == "__main__":
    main()
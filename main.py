import cv2 as opencv
import numpy
from setting import *

ball_pos = [screen_width // 2, screen_height // 2]
ball_velocity = [ball_speed, ball_speed]

player_pos = screen_height // 2 - paddle_height // 2
enemy_pos = screen_height // 2 - paddle_height // 2

def init_game():
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)


def update_game(key):
    global player_pos, enemy_pos

    if key == ord('w') and player_pos > 0:
        player_pos -= player_speed
    if key == ord('s') and player_pos < screen_height - paddle_height:
        player_pos += player_speed
    if key == ord('o') and enemy_pos > 0:
        enemy_pos -= player_speed
    if key == ord('l') and enemy_pos < screen_height - paddle_height:
        enemy_pos += player_speed


def draw_game():
    # Create scene background
    scene = numpy.full((screen_height, screen_width, 3), Mint, dtype=numpy.uint8)

    # Draw paddles
    opencv.rectangle(scene, (paddle_margin, player_pos),
                     (paddle_margin + paddle_width, player_pos + paddle_height), Snow, -1)
    opencv.rectangle(scene, (screen_width - paddle_margin - paddle_width, enemy_pos),
                     (screen_width - paddle_margin, enemy_pos + paddle_height), Snow, -1)

    # Draw ball
    opencv.circle(scene, tuple(ball_pos), ball_size, Gold, -1)

    # Display scores
    font = opencv.FONT_HERSHEY_SIMPLEX
    opencv.putText(scene, "0", (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, Snow, 2)
    opencv.putText(scene, "0", (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, Snow, 2)

    return scene


def main():
    init_game()

    while True:
        key = opencv.waitKey(1) & 0xFF

        update_game(key)
        scene = draw_game()

        if key == ESC_KEY:
            break

        opencv.imshow(game_name, scene)

    opencv.destroyAllWindows()


if __name__ == "__main__":
    main()
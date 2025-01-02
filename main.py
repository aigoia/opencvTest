import cv2 as opencv
import asyncio
import numpy
from pynput.keyboard import Key, Listener  
from setting import *
from paddle import Paddle
from enemy_paddle import EnemyPaddle
from ball import Ball

key_out = False
key_up = False
key_down = False

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player = Paddle(screen_width - paddle_width - paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, player_speed)
enemy = EnemyPaddle(paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, cpu_speed)

def init_game():
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)

def update_game():
    if key_up == True and player.y > 0:
        player.y = player.y - player.speed
    if key_down == True and player.y + player.height < screen_height:
        player.y = player.y + player.speed

    enemy.update(ball.y)
    ball.update()

def draw_game():
    # Create scene background
    scene = numpy.full((screen_height, screen_width, 3), MINT, dtype=numpy.uint8) # uint8 is 0 ~ 255
    opencv.line(scene, (screen_width // 2, 0), (screen_width // 2, screen_height), SNOW, 2)
    
    # Draw objects
    player.draw(scene, SNOW)
    enemy.draw(scene, SNOW)
    ball.draw(scene)

    # Display scores
    font = opencv.FONT_HERSHEY_SIMPLEX
    opencv.putText(scene, "0", (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)
    opencv.putText(scene, "0", (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)

    return scene

def on_press(key):
    global key_up
    global key_down  
    
    key_up = key == Key.up
    key_down = key == Key.down

async def main():
    init_game()
    
    with Listener(on_press=on_press) as listener:
        while True:
            key = opencv.waitKey(delay) & KEY_MASK

            update_game()
            scene = draw_game()
            
            if key == KEY_ESC:
                break

            opencv.imshow(game_name, scene)
    
    opencv.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(main())
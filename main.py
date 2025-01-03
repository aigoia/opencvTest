import cv2 as opencv
import asyncio
import numpy
import sys
from pynput.keyboard import Key, Listener  
from setting import *
from paddle import Paddle
from enemy_paddle import EnemyPaddle
from ball import Ball
from helper import *

init_done = False
key_states = {"up": False, "down": False}

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player = Paddle(screen_width - paddle_width - paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, player_speed)
enemy = EnemyPaddle(paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, cpu_speed)

def init_game():
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)
    
    pause_scene()
    global init_done
    init_done = True
    
def pause_scene():
    while True:
        key = opencv.waitKey(delay) & KEY_MASK
        scene = draw_pause()
        
        if key == KEY_SPACE or key == KEY_ENTER:
            break
        if key == KEY_ESC:
            sys.exit()

        opencv.imshow(game_name, scene)
    
def check_game():    
    if  ball.check_out_of_bounds():
        pause_scene()
        pass

def update_game():
    if key_states["up"] == True and player.y > 0:
        player.y = player.y - player.speed
    if key_states["down"] == True and player.y + player.height < screen_height:
        player.y = player.y + player.speed

    enemy.update(ball.y)
    ball.update()
    check_game()
    
    if check_collision_circle_rectangle((ball.x, ball.y), ball.radius,
                                        (player.x, player.y, player.width, player.height)):
        ball.speed_x = ball.speed_x * -1
    if check_collision_circle_rectangle((ball.x, ball.y), ball.radius,
                                        (enemy.x, enemy.y, enemy.width, enemy.height)):
        ball.speed_x = ball.speed_x * -1

def draw_pause():
    # Create scene background
    scene = numpy.full((screen_height, screen_width, 3), SNOW, dtype=numpy.uint8) # uint8 is 0 ~ 255
    
    font = opencv.FONT_HERSHEY_SIMPLEX
    opencv.putText(scene, pause_string, (screen_width // 2 - score_margin * 4, screen_height // 2 - score_margin // 2), font, 1.5, MINT, 2)

    global init_done
    if init_done:
        opencv.putText(scene, str(ball.player_score), (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, MINT, 2)
        opencv.putText(scene, str(ball.enemy_score), (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, MINT, 2)
    
    return scene

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

    opencv.putText(scene, str(ball.player_score), (screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)
    opencv.putText(scene, str(ball.enemy_score), (3 * screen_width // 4 - score_size // 4, score_margin * 4), font, 1.5, SNOW, 2)

    return scene
    
def on_press(key):
    try:
        if key == Key.up:
            key_states["up"] = True
            key_states["down"] = False
        if key == Key.down:
            key_states["down"] = True
            key_states["up"] = False

    except AttributeError:
        pass

def on_release(key):
    try:
        if key == Key.up:
            key_states["up"] = False
        if key == Key.down:
            key_states["down"] = False

    except AttributeError:
        pass

async def main():
    global key_up, key_down
    init_game()
    # move_more = 0
    
    # Game loop
    with Listener(on_press=on_press, on_release=on_release) as listener:
    
        while True:
            key = opencv.waitKey(delay) & KEY_MASK

            update_game()
            scene = draw_game()
            
            if key == KEY_ESC:
                sys.exit()
            
            opencv.imshow(game_name, scene)
    
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())
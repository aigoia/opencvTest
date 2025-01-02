import cv2 as opencv
import numpy
from pynput.keyboard import Key, Listener  
from setting import *
from paddle import Paddle
from enemy_paddle import EnemyPaddle
from ball import Ball

out = False

ball = Ball(screen_width // 2, screen_height // 2, ball_size, ball_speed, ball_speed)
player = Paddle(screen_width - paddle_width - paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, player_speed)
enemy = EnemyPaddle(paddle_margin, (screen_height - paddle_height) // 2, paddle_width, paddle_height, cpu_speed)

def init_game():
    opencv.namedWindow(game_name, opencv.WINDOW_GUI_NORMAL)
    opencv.resizeWindow(game_name, screen_width, screen_height)

def update_game(key):
    # player.move(key)
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
    if key == Key.up:
        player.move_up  
        print("Up arrow key pressed")
    if key == Key.down:
        player.move_down
        print(player.y)  
        print("Down arrow key pressed") 
    
    if key == Key.esc:
        global out
        out = True

def main():
    init_game()
    
    with Listener(on_press=on_press) as listener:
        while True:
            key = opencv.waitKey(delay)

            update_game(key)
            scene = draw_game()
            
            if out == True:
                break

            opencv.imshow(game_name, scene)
    
    opencv.destroyAllWindows()

if __name__ == "__main__":
    main()
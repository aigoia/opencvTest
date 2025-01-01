import cv2 as opencv
from setting import *

class Paddle:
    def __init__(self, x_pos, screen_height, paddle_width, paddle_height, paddle_speed, paddle_margin):
        self.x_pos = x_pos
        self.y_pos = screen_height // 2 - paddle_height // 2
        self.screen_height = screen_height
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_speed = paddle_speed
        self.paddle_margin = paddle_margin

    def move(self, key):
        if key == KEY_UP and self.y_pos > 0:
            self.y_pos -= self.paddle_speed
        if key == KEY_DOWN and self.y_pos < self.screen_height - self.paddle_height:
            self.y_pos += self.paddle_speed

    def draw(self, scene, color):
        opencv.rectangle(scene, 
                         (self.x_pos, self.y_pos), 
                         (self.x_pos + self.paddle_width, self.y_pos + self.paddle_height), 
                         color, -1)
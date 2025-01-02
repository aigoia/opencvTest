import cv2 as opencv
from setting import *

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    
    def update(self):
        pass

    def draw(self, scene, color):
        opencv.rectangle(scene, 
                         (self.x, self.y), 
                         (self.x + self.width, self.y + self.height), 
                         color, -1)
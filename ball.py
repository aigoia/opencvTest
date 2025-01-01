import random
import cv2 as opencv
from setting import *

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.player_score = 0
        self.enemy_score = 0

    def update(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        self.handle_wall_collision()

    def handle_wall_collision(self):
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.speed_y = self.speed_y * -1

    def check_out_of_bounds(self):
        if self.x < 0:
            self.reset()
            self.player_score = self.player_score + 1
            return True
        elif self.x > self.screen_width:
            self.reset()
            self.enemy_score = self.enemy_score + 1
            return True
        else:
            return False

    def reset(self):
        print("Current score:", self.player_score, "vs", self.enemy_score)

        positions_y = [2]
        positions_y.append(2 if self.player_score == self.enemy_score else 3)
        positions_y.append(2 if self.player_score == self.enemy_score else 1)
        positions_y = list(filter(lambda i: i != 2, positions_y)) + [2]
        print("Start positions:", positions_y)

        positions_y = [y * self.screen_height // 4 for y in positions_y]

        self.y = random.choice(positions_y)
        self.x = self.screen_width // 2
        self.speed_x = self.speed_x * -1

    def draw(self, scene):
        opencv.circle(scene, (self.x, self.y), self.radius, GOLD, -1)
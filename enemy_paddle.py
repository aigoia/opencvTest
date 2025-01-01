from paddle import Paddle
from setting import *

class EnemyPaddle(Paddle):
    def update(self, ball_y):
        if ball_y < self.y + self.height / 2 and self.y > 0:
            self.y -= self.speed
        elif ball_y > self.y + self.height / 2 and self.y + self.height < screen_height:
            self.y += self.speed

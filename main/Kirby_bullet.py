from pico2d import *
import game_world

class Kirby_bullet:
    image = None
    def __init__(self, x=800,y=10,velocity =5):
        if Kirby_bullet.image == None:
            Kirby_bullet.image = load_image('resource\\kirby\\bullet_level_1.png')
        self.power_level = 2
        self.x = x
        self.y = y
        self.velocity =velocity



    def update(self):
        self.x += self.velocity

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)


from pico2d import *

class Main_charcter:
    def __init__(self):
        self.image = load_image('resource\\kirby\\main_character.png')
        self.dir_x  =0
        self.dir_y =0
        self.x =20
        self.y=60
        self.hp = 3
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 75 , 0, 75 , 70 , self.x,self.y,70,70)

    def update(self):
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5

    def return_character_point(self):
        return self.x,self.y


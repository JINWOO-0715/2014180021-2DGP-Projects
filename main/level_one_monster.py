from pico2d import *
from game_framework import ground_size_w
from level_one_monster_bullet import Level_one_monster_bullet
import game_world
import random


class Level_one_monster:
    image = None

    def __init__(self):
        self.x = ground_size_w + random.randint(1,10)*100
        self.y = random.randint(1, 18) * 50
        self.speed = 2
        self.frame = 1
        self.bullet_draw_time =0
        if Level_one_monster.image is None:
            cho = random.randint(1, 4)
            if cho == 1:
                self.image = load_image('resource\\monster\\monster_bird_red.png')
            elif cho == 2:
                self.image = load_image('resource\\monster\\monster_bird_yellow.png')
            elif cho == 3:
                self.image = load_image('resource\\monster\\monster_bird_blue.png')
            elif cho == 4:
                self.image = load_image('resource\\monster\\monster_bird_green.png')

    def draw(self):
        self.frame = (self.frame + 1) % 1
        self.image.clip_draw(self.frame * 36, 0, 36, 42, self.x, self.y, 60, 60)

    def update(self):
        self.bullet_draw_time+=0.01
        self.x -= self.speed
        if self.x < 10 :
            self.x = ground_size_w + random.randint(1, 10) * 20
            self.y = random.randint(1, 18) * 50

        if self.bullet_draw_time >2 :
            bullets = Level_one_monster_bullet(self.x, self.y)
            game_world.add_object(bullets, 1)
            self.bullet_draw_time =0





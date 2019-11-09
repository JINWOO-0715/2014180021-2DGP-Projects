from pico2d import *
from game_framework import ground_size_w
from boss_moster_bullet import Level_one_monster_bullet
import game_world
import random

bullet = None
t = 0
i = 0
r = 1


class Boss_monster:
    image = None

    def __init__(self):
        self.x = ground_size_w + random.randint(1, 10) * 100
        self.y = random.randint(1, 18) * 50
        self.speed = 2
        self.frame = 1
        self.bullet_count = 0
        self.r = 5
        self.moving_point_x = [(random.randint(600, 1000)) for i in range(10)]
        self.moving_point_y = [(random.randint(0, 800)) for i in range(10)]
        self.bullet_draw_time = 0
        if Boss_monster.image is None:
            self.image = load_image('resource\\monster\\boss_monster_mouse_stand.png')

    def draw(self):
        self.frame = (self.frame + 1) % 1
        self.image.clip_draw(self.frame * 0, 0, 63, 58, self.x, self.y, 100, 100)

    def update(self):
        global t, i, r
        self.bullet_draw_time += 0.01
        t = i / 100
        self.x = (1 - t) * self.moving_point_x[r - 1] + t * self.moving_point_x[r]
        self.y = (1 - t) * self.moving_point_y[r - 1] + t * self.moving_point_y[r]
        r = (r + 1) % 10

        if self.bullet_draw_time > 2:
            self.bullet_count += 18
            bullets = Level_one_monster_bullet(self.x, self.y, 5, 2, self.bullet_count)
            game_world.add_object(bullets, 1)
            if self.bullet_count > 360:
                self.bullet_draw_time = 0
                self.bullet_count = 0

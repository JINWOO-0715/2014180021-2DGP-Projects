from pico2d import *
import game_framework
from level_one_monster_bullet import Level_one_monster_bullet
import game_world
import random

bullet = None

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 3


class Level_one_monster:
    image = None
    dead_image = None

    def __init__(self):
        self.x = game_framework.ground_size_w + random.randint(1, 10) * 100
        self.y = random.randint(1, 18) * 50
        self.speed = 2
        self.frame = 1
        self.bullet_count = 0
        self.r = 5
        self.hp = 1
        self.dir = random.randint(1,4)
        self.bullet_point = []
        self.bullet_draw_time = 0
        self.respawn_time = 0
        if Level_one_monster.image is None:
            cho = random.randint(1, 4)
            if cho == 1:
                self.image = load_image('resource\\monster\\monster_bird_red.png')
                self.dead_image = load_image('resource\\monster\\monster_bird_red_dead.png')
            elif cho == 2:
                self.image = load_image('resource\\monster\\monster_bird_yellow.png')
                self.dead_image = load_image('resource\\monster\\monster_bird_yellow_dead.png')
            elif cho == 3:
                self.image = load_image('resource\\monster\\monster_bird_blue.png')
                self.dead_image = load_image('resource\\monster\\monster_bird_blue_dead.png')
            elif cho == 4:
                self.image = load_image('resource\\monster\\monster_bird_green.png')
                self.dead_image = load_image('resource\\monster\\monster_bird_green_dead.png')


    def draw(self):
        if self.hp <= 0:
            self.dead_image.clip_draw(int(self.frame) * 36, 0, 36, 42, self.x, self.y, 60, 60)
        else:
            self.image.clip_draw(int(self.frame) * 36, 0, 36, 42, self.x, self.y, 60, 60)

    def get_bb(self):
        return self.x - 27, self.y - 25, self.x + 24, self.y + 23

    def update(self):
        self.bullet_draw_time += 0.01
        if self.hp <= 0:
            self.respawn_time += 0.01
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        self.x -= self.speed
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if self.respawn_time > 0.3:
            self.x = game_framework.ground_size_w + random.randint(1, 10) * 20
            self.y = random.randint(1, 18) * 50
            self.hp = 1
            self.respawn_time = 0

        if self.x < 10:
            self.x = game_framework.ground_size_w + random.randint(1, 10) * 20
            self.y = random.randint(1, 18) * 50

        if self.bullet_draw_time > 0.5:
            bullets = Level_one_monster_bullet(self.x, self.y, 5, 1, self.bullet_count)
            self.bullet_point = bullets.get_bb()
            game_world.add_object(bullets, 1)
            self.bullet_draw_time = 0

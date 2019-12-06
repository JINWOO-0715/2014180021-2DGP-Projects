from pico2d import *
import game_framework
from level_two_monster_bullet import Level_two_monster_bullet
import game_world
import random
import main_state

bullet = None

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 3


class Level_two_monster:
    image = None
    dead_image = None

    def __init__(self):
        self.x = game_framework.ground_size_w + random.randint(1, 10) * 100
        self.y = random.randint(1, 17) * 50
        self.speed = 2
        self.frame = 1
        self.bullet_count = 0
        self.r = 5
        self.hp = 1
        self.dir = random.randint(1, 4)
        self.bullet_point = []
        self.bullet_draw_time = 0
        self.respawn_time = 0
        if Level_two_monster.image is None:
            cho = random.randint(1, 2)
            if cho == 1:
                self.image = load_image('resource\\monster\\monster_sheep.png')
                self.dead_image = load_image('resource\\monster\\dead.png')
            elif cho == 2:
                self.image = load_image('resource\\monster\\monster_cloud_white.png')
                self.dead_image = load_image('resource\\monster\\dead.png')

    def draw (self):
        if main_state.time > 150:
            if self.hp <= 0:
                #draw_rectangle(*self.get_bb())
                self.dead_image.clip_draw(int(self.frame) * 126, 0, 126, 122, self.x, self.y, 60, 60)
            else:
                #draw_rectangle(*self.get_bb())
                self.image.clip_draw(int(self.frame) * 55, 0, 55, 42, self.x, self.y, 80, 70)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def update(self):
        if main_state.time>150:
            self.bullet_draw_time += 0.01
            if self.hp <= 0:
                self.respawn_time += 0.01
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
            self.x -= self.speed
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

            if self.respawn_time > 0.3:
                self.x = game_framework.ground_size_w + random.randint(1, 10) * 20
                self.y = random.randint(1, 18) * 50
                self.hp = 1
                self.respawn_time = 0

            if self.x < 10:
                self.x = game_framework.ground_size_w + random.randint(1, 10) * 20
                self.y = random.randint(1, 18) * 50

            if self.bullet_draw_time > 0.5:
                bullets = Level_two_monster_bullet(self.x, self.y, 20, random.randint(1,2), self.bullet_count, main_state.kirby.x,
                                                   main_state.kirby.y)
                self.bullet_point = bullets.get_bb()
                game_world.add_object(bullets, 1)
                self.bullet_draw_time = 0

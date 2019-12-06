from pico2d import *
import game_framework
from boss_moster_bullet import Level_one_monster_bullet
import game_world
import random
import main_state

bullet = None
t = 0
i = 0
r = 1

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 10


class Boss_monster:
    image = None

    def __init__(self):
        self.x = game_framework.ground_size_w + random.randint(5, 10) * 100
        self.y = random.randint(1, 18) * 50
        self.speed = 2
        self.frame = 1
        self.bullet_count = 0
        self.skill_use_state = 0
        self.r = 5
        self.hp = 700
        self.moving_point_x = [(random.randint(600, 1000)) for i in range(10)]
        self.moving_point_y = [(random.randint(0, 800)) for i in range(10)]
        self.bullet_draw_time = 0
        self.font = load_font('resource\\DungGeunMo.TTF', 30)
        if Boss_monster.image is None:
            self.image = load_image('resource\\monster\\boss_monster_mouse_stand.png')
            self.dead = load_image('resource\\monster\\boss_monster_mouse_stand.png')

    def get_bb(self):

        return self.x - 45, self.y - 45, self.x + 45, self.y + 45

    def draw(self):
        if main_state.time > 400:
            self.image.clip_draw(int(self.frame) * 63, 0, 60, 74, self.x, self.y, 100, 100)
            draw_rectangle(*self.get_bb())
            self.font.draw(self.x-10, self.y + 45, ' HP : %d' % self.hp, (3, 15, 4))
            if self.skill_use_state:
                self.dead.clip_draw(int(self.frame) * 75, 0, 75, 59, self.x, self.y, 100, 100)


    def update(self):
        global t, i, r
        if main_state.time > 500:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            self.bullet_draw_time += 0.01
            i += 1
            t = i / 100
            self.x = (1 - t) * self.moving_point_x[r - 1] + t * self.moving_point_x[r]
            self.y = (1 - t) * self.moving_point_y[r - 1] + t * self.moving_point_y[r]
            if (i > 101):
                r = (r + 1) % 10
                i = 0
            if self.bullet_draw_time > 0.5:
                bullet_patterns = random.randint(1, 3)
                if bullet_patterns == 1:
                    bullets = [Level_one_monster_bullet() for i in range(10)]
                    for bullet in bullets:
                        bullet.x = self.x
                        bullet.y = random.randint(40, 800)
                        game_world.add_object(bullet, 1)
                    self.bullet_draw_time = 0
                    self.bullet_count = 0
                elif bullet_patterns == 2:
                    while self.bullet_count < 360:
                        self.bullet_count += 18
                        bullets = Level_one_monster_bullet(self.x, self.y, 5, bullet_patterns, self.bullet_count)
                        game_world.add_object(bullets, 1)
                    self.bullet_draw_time = 0
                    self.bullet_count = 0
                elif bullet_patterns == 3:
                    bullets = [Level_one_monster_bullet(self.x, self.y, 5, 3, self.bullet_count, (main_state.kirby.x-120),main_state.kirby.y) for i in range(20)]
                    for bullet in bullets:
                        bullet.y = random.randint(40,game_framework.ground_size_h-40)
                    game_world.add_objects(bullets, 1)
                    self.bullet_draw_time = 0


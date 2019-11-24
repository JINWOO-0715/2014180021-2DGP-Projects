from pico2d import *
import game_world
import game_framework
import math
import main_state

class Level_one_monster_bullet:
    image = None

    def __init__(self, x=800, y=10, velocity=5, bullet_patterns=1 , round_bullet_count =18 ,target_x=40 , target_y=300):
        if Level_one_monster_bullet.image is None:
            Level_one_monster_bullet.image = load_image('resource\\monster\\monster_bullet_1.png')
        self.bullet_patterns = bullet_patterns
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.r = 10
        self.i =0.0
        self.t =0
        self.bullet_count = 0
        self.velocity = velocity
        self.round_bullet_count =round_bullet_count

    def update(self):
        if self.bullet_patterns == 1:
            self.x -= self.velocity
        elif self.bullet_patterns == 2:
            self.r = 3

        if self.x < 10 or self.x > game_framework.ground_size_w - 25 or main_state.kirby_life<0:
            game_world.remove_object(self)
        if main_state.collide(self, main_state.kirby):
            main_state.kirby_life -= 1
            game_world.remove_object(self)

    def get_bb(self):
        return self.x -12 , self.y -10 , self.x+10 , self.y+10

    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.bullet_patterns == 1:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
        elif self.bullet_patterns == 2:
            angle = self.round_bullet_count * 3.141592 / 180
            self.x = self.x+ self.r * math.cos(angle)
            self.y = self.y+ self.r * math.sin(angle)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
        elif self.bullet_patterns ==3:
                self.i += 0.1
                self.t = self.i / 100
                self.x = (1 - self.t) * self.x + self.t * self.target_x
                self.y = (1 - self.t) * self.y + self.t * self.target_y
                self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
                if self.target_x - 20 < self.x < self.target_x + 20 and self.target_y - 20 < self.y < self.target_y + 20:
                    game_world.remove_object(self)

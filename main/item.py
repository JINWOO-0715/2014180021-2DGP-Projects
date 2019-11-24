from pico2d import *
import game_world
import game_framework
import main_state


class Item:
    def __init__(self, x=600, y=20, velocity=1, type=1):
        if type == 1:
            self.image = load_image('resource\\item_attack_up.png')
        if type == 2:
            self.image = load_image('resource\\item_hp_up.png')
        self.x = x
        self.y = y
        self.r = 10
        self.item_type = type
        self.velocity =velocity +4

    def update(self):
        self.x -= self.velocity
        if self.x < 100 or self.x > game_framework.ground_size_w - 25 or main_state.kirby_life<0:
            game_world.remove_object(self)
        if main_state.collide(self, main_state.kirby) and main_state.kirby.bullet_level<3:
            if self.item_type == 1:
                main_state.kirby.bullet_level += 1
            elif self.item_type == 2:
                main_state.kirby_life += 10
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.clip_draw(0, 0, 66, 66, self.x, self.y,50,50)


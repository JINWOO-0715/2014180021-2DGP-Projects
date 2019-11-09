from pico2d import *
import game_world
import game_framework
import main_state


class Item:
    def __init__(self, x=600, y=20, velocity=1, type=1):
        if type == 1:
            Item.image = load_image('resource\\item_attack_up.png')
        elif type == 2:
            Item.image = load_image('resource\\item_hp_up.png')
        self.x = x
        self.y = y
        self.r = 10
        self.item_type = type
        self.velocity = velocity - 0.5

    def update(self):
        self.x -= self.velocity
        if self.x < 400 or self.x > game_framework.ground_size_w - 25:
            game_world.remove_object(self)
        if main_state.collide(self, main_state.kirby):
            if self.item_type == 1:
                main_state.kirby.bullet_level += 1
            elif self.item_type == 2:
                main_state.kirby_life += 10
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 33, self.y - 33, self.x + 33, self.y + 33

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(0, 0, 66, 66, self.x, self.y)


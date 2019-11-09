from pico2d import *
import game_world
import game_framework
import main_state
import random
from item import Item

class Kirby_bullet:
    image = None

    def __init__(self, x=800, y=10, velocity=10, bullet_level=1, bullet_dir=1):
        if Kirby_bullet.image is None:
            Kirby_bullet.image = load_image('resource\\kirby\\bullet_level_1.png')
        self.bullet_level = bullet_level
        self.bullet_dir = bullet_dir
        self.x = x
        self.y = y
        self.velocity = velocity
        self.draw_time = 0

    def update(self):
        if self.bullet_level == 1:
            self.x += self.velocity
        if self.x < 25 or self.x > game_framework.ground_size_w - 25:
            game_world.remove_object(self)
        for main_state.level_one_monster in main_state.level_one_monsters:
            if main_state.collide(self, main_state.level_one_monster) and main_state.level_one_monster.hp == 1:
                main_state.level_one_monster.hp -= 1
                main_state.score+=123
                game_world.remove_object(self)
                item_appear_percentage = random.randint(1,2)
                if item_appear_percentage ==1:
                    item_one = Item(self.x,self.y,1,item_appear_percentage)
                    game_world.add_object(item_one,1)
                elif item_appear_percentage ==2:
                    item_one = Item(self.x,self.y,1,item_appear_percentage)
                    game_world.add_object(item_one, 1)


    def get_bb(self):
        return self.x - 14, self.y - 14, self.x + 14, self.y + 14

    def draw(self):
        if self.bullet_level == 1:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y, 30, 30)
        elif self.bullet_level == 2:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y, 30, 30)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y + 40, 30, 30)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y - 40, 30, 30)

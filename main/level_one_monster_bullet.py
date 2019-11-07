from pico2d import *
import game_world
import game_framework


class Level_one_monster_bullet:
    image = None

    def __init__(self, x=800, y=10, velocity=5, bullet_level=1):
        if Level_one_monster_bullet.image is None:
            Level_one_monster_bullet.image = load_image('resource\\monster\\monster_bullet_1.png')
        self.bullet_level = bullet_level
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        if self.bullet_level == 1:
            self.x -= self.velocity
        if self.x < 10 or self.x > game_framework.ground_size_w - 25:
            game_world.remove_object(self)

    def draw(self):
        if self.bullet_level == 1:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
        elif self.bullet_level == 1:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y + 40)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y - 40)

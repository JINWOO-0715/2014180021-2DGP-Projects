from pico2d import *
import game_world
import game_framework
class Kirby_bullet:
    image = None
    def __init__(self, x=800,y=10,velocity =10,bullet_level=1):
        if Kirby_bullet.image == None:
            Kirby_bullet.image = load_image('resource\\kirby\\bullet_level_1.png')
        self.bullet_level = bullet_level
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        if self.bullet_level == 1:
            self.x += self.velocity
        if self.x < 25 or self.x > game_framework.ground_size_w - 25:
            game_world.remove_object(self)

    def draw(self):
        if self.bullet_level==1:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
        elif self.bullet_level==2:
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y+40)
            self.image.clip_draw(0, 0, 30, 30, self.x, self.y-40)


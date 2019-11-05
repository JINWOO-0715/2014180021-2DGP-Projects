
from pico2d import *

class Main_chracter_Bullet:
    def __init__(self):
        self.xy = []
        self.xy_2 = []
        self.xy_2_2 = []
        self.image_level_one = load_image('resorce\\kirby\\bullet_level_1.png')
        self.power_level = 2
        self.x = 0
        self.y = 0

    def update(self):
        pass

    def draw(self):
        if len(self.xy) != 0 and self.power_level == 1:
            for i, bxy in enumerate(self.xy):
                bxy[0] += 10
                self.xy[i][0] = bxy[0]
                if self.power_level == 1:
                    self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy.remove(bxy)
        elif len(self.xy_2) != 0 and self.power_level == 2:
            for i, bxy in enumerate(self.xy):
                bxy[0] += 10
                self.xy[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy.remove(bxy)
            for i, bxy in enumerate(self.xy_2):
                bxy[0] += 10
                bxy[1] += 2
                self.xy_2[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy_2.remove(bxy)
            for i, bxy in enumerate(self.xy_2_2):
                bxy[0] += 10
                bxy[1] -= 2
                self.xy_2_2[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy_2_2.remove(bxy)
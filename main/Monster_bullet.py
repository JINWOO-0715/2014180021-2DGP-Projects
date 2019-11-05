from pico2d import *


import random

class Monster_bullet:
    image = None
    def __init__(self):
        global choice
        self.xy = []
        if Monster_bullet.image ==None:
            Monster_bullet.image =load_image('resource\\monster\\monster_bullet_1.png')
        self.x = 0
        self.y = 0
        self.t =0
        self.speed =5
        self.target_x=0
        self.target_y=0
        self.bullet_type =1
        self.time =0

    def update(self):
        pass

    def draw(self):
        if self.bullet_type ==1:
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    bxy[0] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0:
                        self.xy.remove(bxy)
        elif self.bullet_type ==2:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t ==1:
                    self.t=0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1-self.t)*bxy[0] + self.t*(-1200)
                    bxy[1] = (1-self.t)*bxy[1] + self.t*(200)
                    self.xy[i][0] = bxy[0]
                    self.image.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] >600:
                        self.xy.remove(bxy)
        elif self.bullet_type == 3:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t == 1:
                    self.t = 0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1 - self.t) * bxy[0] + self.t * (-1200)
                    bxy[1] = (1 - self.t) * bxy[1] + self.t * (100)
                    self.xy[i][0] = bxy[0]
                    self.image.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] > 600:
                        self.xy.remove(bxy)
        elif self.bullet_type == 4:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t == 1:
                    self.t = 0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1 - self.t) * bxy[0] + self.t * (-1200)
                    bxy[1] = (1 - self.t) * bxy[1] + self.t * (400)
                    self.xy[i][0] = bxy[0]
                    self.image.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] > 600:
                        self.xy.remove(bxy)

        elif self.bullet_type == 5:  # 유도탄인데 아직 안된다
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    if self.target_x < self.x :
                        bxy[0] -= self.speed
                    if self.target_y < self.y :
                        bxy[1] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0 or bxy[1] < 0:
                        self.xy.remove(bxy)

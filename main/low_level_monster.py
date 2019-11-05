
import game_framework
import Monster_bullet
from pico2d import *
import random

class Monster():
    def __init__(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 2
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time=0
        self.draw_time_plus =0.001
        self.draw_sign = 0
        self.monster_bird_blue = None
        if self.monster_bird_blue ==None:
            cho = random.randint(1,4)
            if cho ==1 :
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_red.png')
            elif cho ==2:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_yellow.png')
            elif cho ==3:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_blue.png')
            elif cho ==4:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_green.png')

        self.bullet = Monster_bullet.Monster_bullet()

    def set_monster_bird_red(self):
        global choice
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_red.png')
        self.bullet =  Monster_bullet.Monster_bullet()

    def set_monster_bird_yellow(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_yellow.png')
        self.bullet =  Monster_bullet.Monster_bullet()

    def set_monster_bird_green(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_green.png')
        self.bullet =  Monster_bullet.Monster_bullet()

    def set_monster_bird_blue(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_blue.png')
        self.bullet =  Monster_bullet.Monster_bullet()

    def draw(self):
        if self.draw_sign ==1:

            self.frame = (self.frame + 1) % 1
            self.monster_bird_blue.clip_draw(self.frame*36,0,36,42,self.x,self.y,60,60)
            self.bullet.draw()
            if(self.bullet_time>3):
                self.bullet.xy.append([self.x, self.y])
                self.bullet_time =0


    def update(self):
        global choice
        self.draw_time +=0.01
        self.bullet_time+=0.01
        if self.draw_time>5:
            self.x -= self.speed
            self.draw_sign=1
            self.bullet_time += 0.01
            self.bullet.update()
            if self.x < 0:
                if(choice == 1):
                    self.set_monster_bird_green()
                elif choice ==2 :
                    self.set_monster_bird_blue()
                elif choice == 3:
                    self.set_monster_bird_red()
                elif choice == 4:
                    self.set_monster_bird_yellow()

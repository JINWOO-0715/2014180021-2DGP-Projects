import random
import json
import os

from pico2d import *

import pause_state
import game_framework
import title_state
import pause_state


name = "MainState"

main_chracter = None
back_ground =None
font = None
main_chracter_bullet = None

blue_monster = None
blue_monsters = None


class Back_ground:
    def __init__(self):
        self.image = load_image('back_ground.png')

    def draw(self):
        self.image.clip_draw(0,0,200,200,game_framework.ground_size_w/2,game_framework.ground_size_h/2,game_framework.ground_size_w,game_framework.ground_size_h)

class Main_charcter:
    def __init__(self):
        self.image = load_image('main_character.png')
        self.dir_x  =0
        self.dir_y =0
        self.x =20
        self.y=60
        self.hp = 3
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 45 , 0, 45 , 45 , self.x,self.y,60,60)

    def update(self):
        self.frame = (self.frame +1) %1
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5
        delay(0.01)

    def return_character_point(self):
        return self.x,self.y
class Main_chracter_Bullet:
    def __init__(self):
        self.xy =[]
        self.image_level_one = load_image('bullet_level_1.png')
        self.image_level_two = load_image('bullet_level_2.png')
        self.image_level_three = load_image('bullet_level_3.png')
        self.power_level =1
        self.x = 0
        self.y = 0


    def update(self):
        pass

    def draw(self):
        if (len(self.xy) != 0):
            for i, bxy in enumerate(self.xy):
                bxy[0] += 10
                self.xy[i][0] = bxy[0]
                if self.power_level == 1:
                    self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                elif self.power_level == 2:
                    self.image_level_two.clip_draw(0, 0, 40, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy.remove(bxy)
class Monster():
    def __init__(self):
        self.x = game_framework.ground_size_w + 50
        self.y = 500
        self.speed = 3
        self.frame = 1
        self.draw_time =0
        self.bullet_time=0
        self.draw_sign = 0
        self.monster_bird_blue =load_image('monster_bird_blue.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_red(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,6)*100
        self.speed = 3
        self.frame = 1
        self.draw_time = 0
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('monster_bird_red.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_yellow(self):
        self.x = game_framework.ground_size_w + 50
        self.y =random.randint(1,6)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = 0
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('monster_bird_yellow.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_green(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,6)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = 0
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('monster_bird_green.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_blue(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1, 6) * 50
        self.speed = 3
        self.frame = 1
        self.draw_time = 0
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('monster_bird_blue.png')
        self.bullet = Monster_bullet()

    def draw(self):
        if self.draw_sign ==1:
            self.frame = (self.frame + 1) % 1
            self.monster_bird_blue.clip_draw(self.frame*36,0,36,42,self.x,self.y,50,50)
            self.bullet.draw()
            if(self.bullet_time>3):
                self.bullet.xy.append([self.x, self.y])
                self.bullet_time =0


    def update(self):
        self.draw_time +=0.01
        self.bullet_time+=0.01
        if self.draw_time>2:
            self.x -= self.speed
            self.draw_sign=1
            self.bullet_time += 0.01
            self.bullet.update()
            if self.x < 0:
                choice =random.randint(1,4)
                if(choice == 1):
                  self.set_monster_bird_green()
                elif choice ==2 :
                    self.set_monster_bird_blue()
                elif choice == 3:
                    self.set_monster_bird_red()
                elif choice == 4:
                    self.set_monster_bird_yellow()


class Monster_bullet:
    def __init__(self):
        self.xy = []
        self.image_level_one = load_image('monster_bullet_1.png')
        self.x = 0
        self.y = 0
        self.speed =5
        self.target_x=0
        self.target_y=0
        self.bullet_type = 0

    def update(self):
        pass

    def draw(self):
        if self.bullet_type ==0 :
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    bxy[0] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0:
                        self.xy.remove(bxy)
        elif self.bullet_type ==1:  # 왼쪽 위 발사
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    bxy[0] -= self.speed
                    bxy[1] += self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0 or bxy[1] >600:
                        self.xy.remove(bxy)
        elif self.bullet_type == 2:  # 왼쪽 위 발사
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    bxy[0] -= self.speed
                    bxy[1] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0 or bxy[1] < 0:
                        self.xy.remove(bxy)
        elif self.bullet_type == 3:  # 유도탄인데 아직 안된다
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    if self.target_x < self.x :
                        bxy[0] -= self.speed
                    if self.target_y < self.y :
                        bxy[1] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0 or bxy[1] < 0:
                        self.xy.remove(bxy)



def enter():
    global main_charcter , back_ground , main_chracter_bullet
    global blue_monster,blue_monsters
    main_charcter = Main_charcter()

    back_ground =Back_ground()
    main_chracter_bullet = Main_chracter_Bullet()
    blue_monster = Monster()
    blue_monsters = [Monster() for i in range(10)]
    size = 60
    for blue_monster in blue_monsters:
        blue_monster.y  -=size
        size+=60


def exit():
    global main_charcter,back_ground ,main_chracter_bullet
    global blue_monster,blue_monsters
    del (main_charcter)
    del (back_ground)
    del (main_chracter_bullet)
    del (blue_monster,blue_monsters)

def pause():
    pass

def resume():
    pass

def handle_events():
    global main_charcter, back_ground, main_chracter_bullet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
          game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
#캐릭터 이동 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            main_charcter.dir_x +=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            main_charcter.dir_x -=1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            main_charcter.dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            main_charcter.dir_y -=1

        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            main_charcter.dir_x -=1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            main_charcter.dir_x += 1

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            main_charcter.dir_y -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            main_charcter.dir_y += 1
#총알 발사 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            main_chracter_bullet.x = main_charcter.x
            main_chracter_bullet.y = main_charcter.y
            main_chracter_bullet.xy.append([main_chracter_bullet.x,main_chracter_bullet.y])


def update():
    main_charcter.update()
    main_chracter_bullet.update()
    for blue_monster in blue_monsters:
        blue_monster.update()




def draw():
    clear_canvas()
    back_ground.draw()
    main_charcter.draw()
    main_chracter_bullet.draw()
    for blue_monster in blue_monsters:
        blue_monster.draw()
    update_canvas()






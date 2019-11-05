import random
import json
import os

from pico2d import *
import Kirby
import Kirby_bullet
import game_framework
import pause_state
import low_level_monster


name = "MainState"


back_ground =None
font = None

kirby = None
kirby_bullet = None
choice =None
blue_monster = None
blue_monsters = None
red_monster = None
red_monsters = None


class Back_ground:
    def __init__(self):
        self.image = load_image('resorce\\back_ground\\back_ground.png')

    def draw(self):
        self.image.clip_draw(0,0,game_framework.ground_size_w,game_framework.ground_size_h,game_framework.ground_size_w/2,game_framework.ground_size_h/2,game_framework.ground_size_w,game_framework.ground_size_h)

def enter():
    global kirby , back_ground , kirby_bullet
    global blue_monster,blue_monsters ,red_monster,red_monsters

    kirby = Kirby.Main_charcter()
    back_ground =Back_ground()
    kirby_bullet = Kirby_bullet.Main_chracter_Bullet()
    blue_monster = low_level_monster.Monster()
    blue_monsters = [low_level_monster.Monster() for i in range(20)]





def exit():
    global kirby,back_ground ,kirby_bullet
    global blue_monster,blue_monsters,red_monster,red_monsters
    del (kirby)
    del (back_ground)
    del (kirby_bullet)
    del (blue_monster,blue_monsters)
    del (red_monster,red_monsters)

def pause():
    pass

def resume():
    pass

def handle_events():
    global kirby, back_ground, kirby_bullet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
#캐릭터 이동 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_x +=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_x -=1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_y -=1

        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            kirby.dir_x -=1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            kirby.dir_x += 1

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            kirby.dir_y -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            kirby.dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            kirby_bullet.power_level = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            kirby_bullet.power_level = 2

#총알 발사 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            kirby_bullet.x = kirby.x
            kirby_bullet.y = kirby.y
            if(kirby_bullet.power_level==1):
                kirby_bullet.xy.append([kirby_bullet.x, kirby_bullet.y])
            elif(kirby_bullet.power_level == 2):
                kirby_bullet.xy.append([kirby_bullet.x, kirby_bullet.y])
                kirby_bullet.xy_2.append([kirby_bullet.x, kirby_bullet.y])
                kirby_bullet.xy_2_2.append([kirby_bullet.x, kirby_bullet.y])

def update():
    global choice
    kirby.update()
    kirby_bullet.update()
    choice = random.randint(1,4)
    for blue_monster in blue_monsters:
        blue_monster.update()




def draw():
    clear_canvas()
    back_ground.draw()
    kirby.draw()
    kirby_bullet.draw()
    for blue_monster in blue_monsters:
        blue_monster.draw()
    update_canvas()






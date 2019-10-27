import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state


name = "MainState"

main_charcter = None
back_ground =None
font = None

class Back_ground:
    def __init__(self):
        self.image = load_image('back_ground.png')

    def draw(self):
        self.image.clip_draw(0,0,1280,800,640,360,1280,720)

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
        self.image.clip_draw(self.frame * 45 , 0, 45 , 45 , self.x,self.y,80,80)

    def update(self):
        self.frame = (self.frame +1) %1
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5
        delay(0.01)



class Bullet:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('curbe.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global main_charcter , back_ground
    main_charcter = Main_charcter()
    back_ground =Back_ground()




def exit():
    global main_charcter,back_ground
    del (main_charcter)
    del (back_ground)



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
          game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)

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



def update():
    main_charcter.update()


def draw():
    clear_canvas()
    back_ground.draw()
    main_charcter.draw()
    update_canvas()






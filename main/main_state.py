import random
import json
import os

from pico2d import *
import game_framework
import game_world
import pause_state

from kirby import Kirby

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
        self.image = load_image('resource\\back_ground\\back_ground.png')
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,game_framework.ground_size_w,game_framework.ground_size_h,game_framework.ground_size_w/2,game_framework.ground_size_h/2,game_framework.ground_size_w,game_framework.ground_size_h)

def enter():
    global kirby , back_ground , kirby_bullet
    global blue_monster,blue_monsters ,red_monster,red_monsters
    back_ground =Back_ground()
    kirby = Kirby()
    game_world.add_object(back_ground,0)
    game_world.add_object(kirby,1)

def exit():
    game_world.clear()

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
        else:
            kirby.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






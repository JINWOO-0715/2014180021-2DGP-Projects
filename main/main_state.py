import random
import json
import os

from pico2d import *
import game_framework
import game_world
import pause_state
from level_one_monster import Level_one_monster
from kirby import Kirby
from boss_moster import Boss_monster

name = "MainState"

back_ground = None
font = None
kirby = None
kirby_bullet = None
choice = None
boss_monster = None
level_one_monster = None
level_one_monsters = []
kirby_life = 100

class Back_ground:
    def __init__(self):
        self.image = load_image('resource\\back_ground\\back_ground.png')
        self.kirby_life = load_image('resource\\kirby\\life.png')
        self.font = load_font('resource\\DungGeunMo.TTF',30)


    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, game_framework.ground_size_w, game_framework.ground_size_h,
                             game_framework.ground_size_w / 2, game_framework.ground_size_h / 2,
                             game_framework.ground_size_w, game_framework.ground_size_h)
        self.kirby_life.clip_draw(0,0,30,31, game_framework.ground_size_w/10-80, game_framework.ground_size_h-70,50,50)
        self.font.draw(game_framework.ground_size_w/10-55, game_framework.ground_size_h-70,' X %d' % kirby_life,(255,0,0))



def enter():
    global kirby, back_ground
    global  level_one_monsters
    back_ground = Back_ground()
    kirby = Kirby()
    level_one_monsters = [Level_one_monster() for i in range(20)]
    boss_monster = Boss_monster()
    game_world.add_object(back_ground, 0)
    game_world.add_object(kirby, 1)
    game_world.add_objects(level_one_monsters, 1)




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
    for level_one_monster in level_one_monsters:
        if collide(kirby, level_one_monster):
           global kirby_life
           kirby_life-= 1
    delay(0.01)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
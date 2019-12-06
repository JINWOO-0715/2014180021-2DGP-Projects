import random
import json
import os

from pico2d import *
import game_framework
import game_world
import pause_state
from level_one_monster import Level_one_monster_go_left
from level_two_monster import Level_two_monster
from Kirby import Kirby
from boss_moster import Boss_monster
import dead_state

name = "MainState"


back_ground = None
font = None

kirby_bullet = None
choice = None

level_one_monster = None
level_one_monsters = []
level_two_monster = None
level_two_monsters = []
kirby_life = 0
score = 0
time = 0
time_start_sign =False
stage_two_sign =True
boss_monster =None


class Back_ground:
    def __init__(self):
        self.image = load_image('resource\\back_ground\\back_ground.png')
        self.kirby_life = load_image('resource\\kirby\\life.png')
        self.font = load_font('resource\\DungGeunMo.TTF', 30)
        self.bgm = load_wav('main_bgm.wav')
        self.bgm.set_volume(60)
        self.bgm.play()


    def update(self):
        pass

    def draw(self):
        global kirby
        self.image.clip_draw(0, 0, game_framework.ground_size_w, game_framework.ground_size_h,
                             game_framework.ground_size_w / 2, game_framework.ground_size_h / 2,
                             game_framework.ground_size_w, game_framework.ground_size_h)
        self.kirby_life.clip_draw(0, 0, 30, 31, game_framework.ground_size_w / 10 - 80,
                                  game_framework.ground_size_h - 70, 50, 50)
        self.font.draw(kirby.x ,kirby.y+15 ,' X %d' % kirby_life,
                       (255, 0, 0))
        self.font.draw(game_framework.ground_size_w / 10 - 90, game_framework.ground_size_h - 110, ' Score %d' % score,
                       (255, 0, 0))
        self.font.draw(600, 750, ' Time %d' % time, (255, 0, 0))

def enter():
    global kirby, back_ground,kirby_life ,score,time
    global level_one_monsters, boss_monster ,time_start_sign ,level_two_monsters
    kirby_life =1000
    back_ground = Back_ground()
    kirby = Kirby()
    level_one_monsters = [Level_one_monster_go_left() for i in range(20)]
    level_two_monsters = [Level_two_monster() for i in range(20)]
    boss_monster = Boss_monster()
    game_world.add_object(back_ground, 0)
    game_world.add_object(kirby, 1)
    game_world.add_object(boss_monster, 1)
    game_world.add_objects(level_two_monsters, 1)
    game_world.add_objects(level_one_monsters, 1)
    time_start_sign = True

    score = 0
    time = 0


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global kirby, back_ground, kirby_bullet ,time_start_sign
    global kirby_life ,time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            time_start_sign = False
            game_framework.push_state(pause_state)
        else:
            kirby.handle_event(event)


def update():
    global time ,level_two_monsters ,stage_two_sign , kirby_life , boss_monster,kirby
    for game_object in game_world.all_objects():
        game_object.update()
    for level_one_monster in level_one_monsters:
        if collide(kirby, level_one_monster):
            kirby_life -= 1
    for level_two_monster in level_two_monsters:
        if collide(kirby, level_two_monster):
            kirby_life -= 1
    if collide(kirby, boss_monster):
        kirby_life -= 1
    if time_start_sign:
        time += get_time()-(get_time()-0.1)
    if time >150:
        for level_one_monster in level_one_monsters:
            game_world.remove_object(level_one_monster)
    if time >300:
        for level_two_monster in level_two_monsters:
            game_world.remove_object(level_two_monster)
    if kirby_life<0:
        game_world.remove_object(boss_monster)
        game_world.remove_object(kirby)
        game_framework.change_state(dead_state)

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

import game_framework
from pico2d import *
import main_state

import story1
name = "title_state"
image = None


def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del (image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(story1)


def draw():
    clear_canvas()
    image.draw(game_framework.ground_size_w/2, game_framework.ground_size_h/2 , game_framework.ground_size_w,game_framework.ground_size_h)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass







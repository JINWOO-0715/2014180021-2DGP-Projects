import game_framework
from pico2d import *


import title_state
name = "title_state"

state = 0


def enter():
    global image
    image = load_image('resource\\back_ground\\guide.png')


def exit():
    global image
    del (image)


def handle_events():
    global state
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()


def draw():
    clear_canvas()
    image.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                   game_framework.ground_size_h)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass







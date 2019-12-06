import game_framework
from pico2d import *

import title_state

name = "title_state"

state = 0
font = None


def enter():
    global image, font
    image = load_image('resource\\back_ground\\NULL.png')
    font = load_font('resource\\DungGeunMo.TTF', 80)


def exit():
    global image, font
    del (image)
    del (font)


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
    font.draw(300, 750, 'W ', (0, 0, 0))
    font.draw(200, 650, 'a ', (0, 0, 0))
    font.draw(300, 650, 's ', (0, 0, 0))
    font.draw(400, 650, 'd ', (0, 0, 0))

    font.draw(600, 650, '공격키 4방향 ', (0, 0, 0))

    font.draw(300, 400, '↑', (0, 0, 0))
    font.draw(200, 300, '←', (0, 0, 0))
    font.draw(300, 300, '↓', (0, 0, 0))
    font.draw(400, 300, '→', (0, 0, 0))

    font.draw(600, 300, '움직이기 4방향 ', (0, 0, 0))

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

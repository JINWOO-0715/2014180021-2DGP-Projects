from pico2d import *

import game_framework
import main_state


name = "pause_state"
image = None
count = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del (image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def draw():
    clear_canvas()
    if count <= 20:
        image.clip_draw(200, 200, 500, 500,  game_framework.ground_size_w/2, game_framework.ground_size_h/2, game_framework.ground_size_w/2, game_framework.ground_size_h/2)
    update_canvas()
    delay(0.05)

def update():
    global count
    count += 1
    if count == 40:
        count = 0


def pause():
    pass


def resume():
    pass







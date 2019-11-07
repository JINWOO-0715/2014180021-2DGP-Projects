from pico2d import *

import game_framework
import main_state


name = "pause_state"
image = None
image_2 =None
state = 0

def enter():
    global image, image_2
    image = load_image('resource\\back_ground\\pause_state_1.png')
    image_2 = load_image('resource\\back_ground\\pause_state_2.png')

def exit():
    global image ,image_2
    del (image)
    del (image_2)

def handle_events():
    global state
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if (state % 2 == 0):
                game_framework.pop_state()
            elif (state % 2 == 1):
                game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            state += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            state += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            if (state % 2 == 0):
                game_framework.pop_state()
            elif (state % 2 == 1):
                game_framework.quit()





def draw():
    clear_canvas()
    if  state%2==0 :
        image.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                   game_framework.ground_size_h)
    elif state%2==1 :
        image_2.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                   game_framework.ground_size_h)

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass







import game_framework
from pico2d import *
import guide_state
import main_state


name = "title_state"
image = None
image_2 = None
image_3 = None
state = 0
title_sound = None

def enter():
    global image, image_2, image_3,title_sound

    title_sound = load_music('resource\\sound\\Title_1.mp3')
    image = load_image('resource\\back_ground\\title_sean_1.png')
    image_2 = load_image('resource\\back_ground\\title_sean_2.png')
    image_3 = load_image('resource\\back_ground\\title_sean_3.png')
    title_sound.set_volume(40)
    title_sound.play()



def exit():
    global image, image_2, image_3 ,title_sound
    del (image)
    del (image_2)
    del (image_3)
    del (title_sound)


def handle_events():
    global state
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if (state % 3 == 0):
                game_framework.change_state(main_state)
            elif state % 3 == 1:
                game_framework.push_state(guide_state)
            elif state % 3 == 2:
                game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            state += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            state -= 1


def draw():
    clear_canvas()
    if state % 3 == 0:
        image.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                   game_framework.ground_size_h)
    elif state % 3 == 1:
        image_2.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                     game_framework.ground_size_h)
    elif state % 3 == 2:
        image_3.draw(game_framework.ground_size_w / 2, game_framework.ground_size_h / 2, game_framework.ground_size_w,
                     game_framework.ground_size_h)
    update_canvas()


def update():
    global  title_sound

    pass


def pause():
    pass


def resume():
    pass

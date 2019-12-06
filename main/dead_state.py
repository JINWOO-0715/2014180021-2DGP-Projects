import game_framework
import game_world
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global dead_sound
    global image
    image = load_image("resource\\back_ground\\game_over.png")
    #dead_sound.set_volume(64)
    #dead_sound.play()



def exit():
    global image ,dead_sound
    del (image)
    #del (dead_sound)


def update():
    global logo_time , sound

    if (logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    logo_time += 0.01



def draw():
    global image
    clear_canvas()
    image.draw(game_framework.ground_size_w/2, game_framework.ground_size_h/2,game_framework.ground_size_w, game_framework.ground_size_h)
    update_canvas()



def handle_events():
    pass


def pause(): pass


def resume(): pass





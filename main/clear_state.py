import game_framework
import game_world
from pico2d import *
import title_state

name = "StartState"
image = None

clear_stage =None

def enter():
    global dead_sound ,clear_stage
    global image
    image = load_image("resource\\back_ground\\win.png")
    clear_stage = load_music("resource\\sound\\clear.mp3")
    clear_stage.set_volume(64)
    clear_stage.play()



def exit():
    global image ,clear_stage
    del (image)
    del (clear_stage)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)



def draw():
    global image
    clear_canvas()
    image.draw(game_framework.ground_size_w/2, game_framework.ground_size_h/2,game_framework.ground_size_w, game_framework.ground_size_h)
    update_canvas()



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(title_state)


def pause(): pass


def resume(): pass





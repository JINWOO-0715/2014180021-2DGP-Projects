from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}
class IdleState:
    @staticmethod
    def enter(kirby, event):
        if event == RIGHT_DOWN:
            kirby.dir_x += 1
        elif event == LEFT_DOWN:
            kirby.dir_x -= 1
        elif event == RIGHT_UP:
            kirby.dir_x -= 1
        elif event == LEFT_UP:
            kirby.dir_x += 1
        elif event == UP_UP:
            kirby.dir_y -= 1
        elif event == UP_DOWN:
            kirby.dir_y += 1
        elif event == DOWN_UP:
            kirby.dir_y += 1
        elif event == DOWN_DOWN:
            kirby.dir_y -= 1

    @staticmethod
    def exit(boy, event):
        # fill here
        pass

    @staticmethod
    def do(kirby):
        kirby.x += kirby.dir_x
        kirby.x = clamp(25, kirby.x, 1280 - 25)
        kirby.y += kirby.dir_y
        kirby.y = clamp(25, kirby.y, 850 - 25)
        # fill here

    @staticmethod
    def draw(kirby):
        if kirby.dir_x == 1:
            kirby.image.clip_draw(kirby.frame * 75 , 0, 75 , 70, kirby.x, kirby.y,70,70)
        else:
            kirby.image.clip_draw(kirby.frame * 75, 0, 75, 70, kirby.x, kirby.y, 70, 70)


class RunState:

    @staticmethod
    def enter(kirby, event):
        if event == RIGHT_DOWN:
            kirby.dir_x += 1
        elif event == LEFT_DOWN:
            kirby.dir_x -= 1
        elif event == RIGHT_UP:
            kirby.dir_x -= 1
        elif event == LEFT_UP:
            kirby.dir_x += 1
        elif event == UP_UP:
            kirby.dir_y -= 1
        elif event == UP_DOWN:
            kirby.dir_y += 1
        elif event == DOWN_UP:
            kirby.dir_y += 1
        elif event == DOWN_DOWN:
            kirby.dir_y -= 1

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(kirby):
        kirby.x += kirby.dir_x
        kirby.x = clamp(25, kirby.x, 1280 - 25)
        kirby.y += kirby.dir_y
        kirby.y = clamp(25, kirby.y, 850 - 25)

    @staticmethod
    def draw(kirby):
        kirby.image.clip_draw(kirby.frame * 75 , 75, 75 , 70, kirby.x, kirby.y,70,70)



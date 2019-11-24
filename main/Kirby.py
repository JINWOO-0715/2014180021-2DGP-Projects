from pico2d import *

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 3
import game_framework
import game_world
from kirby_bullet import Kirby_bullet
from kirby_state import IdleState
from kirby_state import RunState

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, SPACE, D_DOWN, S_DOWN, A_DOWN, W_DOWN = range(13)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_w): W_DOWN,
}

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,
               SPACE:IdleState  , D_DOWN:IdleState ,A_DOWN:IdleState , W_DOWN:IdleState ,S_DOWN:IdleState  },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,
              SPACE :RunState ,D_DOWN:RunState ,A_DOWN:RunState ,S_DOWN:IdleState ,W_DOWN:IdleState },
}


class Kirby:
    def __init__(self):
        self.image = load_image('resource\\kirby\\main_character.png')
        self.dir_x = 0
        self.dir_y = 0
        self.x = 20
        self.y = 300
        self.frame = 0
        self.bullet_level = 1
        self.bullet_dir =1
        self.velocity =0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def get_bb(self):
        return self.x -20 , self.y -20 , self.x+20 , self.y+20

    def draw(self):
        self.image.clip_draw(int(self.frame) * 75, 0, 75, 70, self.x, self.y, 60, 60)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def bullet(self):
        if self.bullet_level == 1:
            bullets = Kirby_bullet(self.x, self.y, 10, self.bullet_level, self.bullet_dir)
            game_world.add_object(bullets, 1)
        if self.bullet_level == 2:
           if self.bullet_dir ==1 or self.bullet_dir ==3:
                bullets = Kirby_bullet(self.x, self.y, 10, self.bullet_level, self.bullet_dir)
                bullets_two = Kirby_bullet(self.x, self.y+40, 10, self.bullet_level, self.bullet_dir)
                bullets_tri = Kirby_bullet(self.x, self.y-40, 10, self.bullet_level, self.bullet_dir)
                game_world.add_object(bullets, 1)
                game_world.add_object(bullets_two, 1)
                game_world.add_object(bullets_tri, 1)
           if self.bullet_dir ==2 or self.bullet_dir ==4:
                bullets = Kirby_bullet(self.x, self.y, 10, self.bullet_level, self.bullet_dir)
                bullets_two = Kirby_bullet(self.x+ 40, self.y , 10, self.bullet_level, self.bullet_dir)
                bullets_tri = Kirby_bullet(self.x- 40, self.y , 10, self.bullet_level, self.bullet_dir)
                game_world.add_object(bullets, 1)
                game_world.add_object(bullets_two, 1)
                game_world.add_object(bullets_tri, 1)
        if self.bullet_level ==3:
            if self.bullet_dir == 1 or self.bullet_dir == 3:
                bullets = Kirby_bullet(self.x, self.y, 10, self.bullet_level, self.bullet_dir)
                bullets_two = Kirby_bullet(self.x, self.y+40 , 10, self.bullet_level,self.bullet_dir)
                bullets_tri = Kirby_bullet(self.x, self.y-40, 10, self.bullet_level, self.bullet_dir)
                bullets_fou = Kirby_bullet(self.x, self.y+100 , 10, self.bullet_level, self.bullet_dir)
                bullets_fiv = Kirby_bullet(self.x, self.y -100, 10, self.bullet_level, self.bullet_dir)
                game_world.add_object(bullets, 1)
                game_world.add_object(bullets_two, 1)
                game_world.add_object(bullets_tri, 1)
                game_world.add_object(bullets_fou, 1)
                game_world.add_object(bullets_fiv, 1)
            if self.bullet_dir == 2 or self.bullet_dir == 4:
                bullets = Kirby_bullet(self.x, self.y, 10, self.bullet_level, self.bullet_dir)
                bullets_two = Kirby_bullet(self.x+40, self.y , 10, self.bullet_level,self.bullet_dir)
                bullets_tri = Kirby_bullet(self.x-40, self.y, 10, self.bullet_level, self.bullet_dir)
                bullets_fou = Kirby_bullet(self.x+100, self.y , 10, self.bullet_level, self.bullet_dir)
                bullets_fiv = Kirby_bullet(self.x-100, self.y , 10, self.bullet_level, self.bullet_dir)
                game_world.add_object(bullets, 1)
                game_world.add_object(bullets_two, 1)
                game_world.add_object(bullets_tri, 1)
                game_world.add_object(bullets_fou, 1)
                game_world.add_object(bullets_fiv, 1)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def collide(a, b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True


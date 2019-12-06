from pico2d import *
import game_framework
import game_world
import random



class Sound:

    def __init__(self):
        self.monster_dead_sound = load_wav('resource\\sound\\bird_dead.wav')
        self.monster_dead_sound.set_volume(40)

    def draw(self):
        pass

    def update(self):
        pass

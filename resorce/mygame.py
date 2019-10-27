import game_framework
import pico2d
import start_state

pico2d.open_canvas(game_framework.ground_size_w,game_framework.ground_size_h)
game_framework.run(start_state)
pico2d.close_canvas()

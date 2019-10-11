from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('bullet_level_2.png')
speed = 10
def Move_right():
    x,y = 0+25,90
    frame=0
    while (x < 800-25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 21, 0, 21, 15, x, 90)
        update_canvas()
        frame = (frame + 1) % 1
        x += speed
        delay(0.05)
        get_events()
  
def Move_left():
    x,y =800-25,90
    frame=0
    while(x>0+25):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*35,0,35,50,x,90)
        update_canvas()
        frame = (frame+1)%6
        x -= speed
        delay(0.05)
        get_events()

while True:
    Move_right()
    Move_left()

close_canvas()
        
        

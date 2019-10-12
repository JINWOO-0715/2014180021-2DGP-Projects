from pico2d import *
open_canvas()
#boss_monster_mouse_stand size 252 * 58 /4
#boss_monster_skill size 600*74 /10
#main_charcter size 90 * 46 / 2
#monster_ball size 54 * 54 / 1
#monster_bear size 318 * 66 /4
#monster_bird_blue size 214 *42 /6
#monster_red_blue size 214 *42 /6
#monster_green_blue size 214 *42 /6
#monster_yello_blue size 214 *42 /6
#monster_cloud_black size 96*84 / 1
#monster_cloud_puple size  96*84 /1
#monster_cloud_white size  252 *38 / 4
#monster_fire_ball size 538*80 /6
#monster_fish size 52*52
#monster_mouse size 209*34 /3
#monster_plant size 40*28
#monster_sheep size 221*42 /


grass = load_image('grass.png')
character = load_image('monster_sheep.png')
coin = load_image('coin.png')
monster_bear = load_image('monster_bear.png')

def Move_right():
    x,y = 0+25,90
    frame=0
    while (x < 800-25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 55,0, 55, 42, x, 90)
        update_canvas()
        frame = (frame + 1) % 4
        x += 1
        delay(0.05)
        get_events()

def handle_events():
    global sign_move
    global dir_charecter_x
    global dir_charecter_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            sign_move =False
        elif event.type==SDL_KEYDOWN:
            if event.key ==SDLK_RIGHT:
                dir_charecter_x +=1
            elif event.key==SDLK_LEFT:
                dir_charecter_x -=1
            elif event.key == SDLK_UP:
                dir_charecter_y +=1
            elif event.key == SDLK_DOWN:
                dir_charecter_y -=1


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_charecter_x -= 1
            elif event.key == SDLK_LEFT:
                dir_charecter_x += 1
            elif event.key == SDLK_UP:
                dir_charecter_y -= 1
            elif event.key == SDLK_DOWN:
                dir_charecter_y += 1



sign_move = True
c_frame =0
coin_frame =0
x = 0
y=40
dir_charecter_x =0
dir_charecter_y =0

draw_bullet_1 = False

while sign_move:
    clear_canvas()
    Move_right()
    character.clip_draw(c_frame*45,0,45,60,x,y) # 캐릭터 사이즈 35 50 애니 6장
    coin.clip_draw(coin_frame * 23, 0, 23, 40, x, y)  # 캐릭터 사이즈 35 50 애니 6장
    delay(0.1)
    update_canvas()
    handle_events()
    c_frame = (c_frame +1)%1
    coin_frame = (coin_frame +1)%6
    x += dir_charecter_x * 5
    y += dir_charecter_y * 5
    delay(0.01)



close_canvas()
        
        

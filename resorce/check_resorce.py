from pico2d import *

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
KPU_WIDTH, KPU_HEIGHT = 1280, 720

open_canvas(KPU_WIDTH,KPU_HEIGHT)
bullet_one = load_image('bullet_level_1.png')
bullet_two = load_image('bullet_level_2.png')

grass = load_image('grass.png')
character = load_image('main_charecter.png')
coin = load_image('coin.png')
monster_bear = load_image('monster_bear.png')
ground_image = load_image('123.png')
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
    global dir_bullet_x
    global dir_bullet_y
    global bullet_y
    global bullet_x
    global character_x
    global character_y
    global bullet_xy

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
            elif event.key ==SDLK_SPACE:
                bullet_x = character_x
                bullet_y = character_y
                bullet_xy.append([bullet_x,bullet_y])




        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_charecter_x -= 1
            elif event.key == SDLK_LEFT:
                dir_charecter_x += 1
            elif event.key == SDLK_UP:
                dir_charecter_y -= 1
            elif event.key == SDLK_DOWN:
                dir_charecter_y += 1
            elif event.key == SDLK_SPACE:
                sign_bullet = False


bullet_xy =[]
c_frame =0
character_x = 0
character_y=40
bullet_x = 0
bullet_y= 0
dir_charecter_x =0
dir_charecter_y =0
dir_bullet_x =100
dir_bullet_y =100
bullet_power=2

count = 0

while True:
    clear_canvas()
    ground_image.draw(KPU_WIDTH//2,KPU_HEIGHT//2)
    character.clip_draw(c_frame*45,0,45,60,character_x,character_y) # 캐릭터 사이즈 35 50 애니 6장
    handle_events()
    c_frame = (c_frame +1)%1
    character_x += dir_charecter_x * 5
    character_y += dir_charecter_y * 5
    if(len(bullet_xy)!=0):
        for i ,bxy in enumerate(bullet_xy):
            bxy[0] += 10
            bullet_xy[i][0] = bxy[0]
            if bullet_power==1:
                bullet_one.clip_draw(0,0,30,30,bxy[0],bxy[1])
            elif bullet_power==2:
                bullet_two.clip_draw(0,0,40,30,bxy[0],bxy[1])
            if bxy[0]>=1280:
                bullet_xy.remove(bxy)

    update_canvas()

    delay(0.01)



close_canvas()
        
        

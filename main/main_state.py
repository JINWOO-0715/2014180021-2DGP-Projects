import random
import json
import os

from pico2d import *
import Kirby
import pause_state
import game_framework
import title_state
import pause_state


name = "MainState"


back_ground =None
font = None
main_chracter_bullet = None
choice =None
blue_monster = None
blue_monsters = None
red_monster = None
red_monsters = None


kirby = None
class Back_ground:
    def __init__(self):
        self.image = load_image('resorce\\back_ground\\back_ground.png')

    def draw(self):
        self.image.clip_draw(0,0,game_framework.ground_size_w,game_framework.ground_size_h,game_framework.ground_size_w/2,game_framework.ground_size_h/2,game_framework.ground_size_w,game_framework.ground_size_h)

class Main_chracter_Bullet:
    def __init__(self):
        self.xy =[]
        self.xy_2 = []
        self.xy_2_2 = []
        self.image_level_one = load_image('resorce\\kirby\\bullet_level_1.png')
        self.power_level =2
        self.x = 0
        self.y = 0


    def update(self):
        pass


    def draw(self):
        if (len(self.xy) != 0 and self.power_level ==1):
            for i, bxy in enumerate(self.xy):
                bxy[0] += 10
                self.xy[i][0] = bxy[0]
                if self.power_level == 1:
                    self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy.remove(bxy)
        elif (len(self.xy_2 ) != 0 and self.power_level ==2):
            for i, bxy in enumerate(self.xy):
                bxy[0] += 10
                self.xy[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280:
                    self.xy.remove(bxy)
            for i, bxy in enumerate(self.xy_2):
                bxy[0] += 10
                bxy[1] += 2
                self.xy_2[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280 :
                    self.xy_2.remove(bxy)
            for i, bxy in enumerate(self.xy_2_2):
                bxy[0] += 10
                bxy[1] -= 2
                self.xy_2_2[i][0] = bxy[0]
                self.image_level_one.clip_draw(0, 0, 30, 30, bxy[0], bxy[1])
                if bxy[0] >= 1280 :
                    self.xy_2_2.remove(bxy)

class Monster():
    def __init__(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 2
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time=0
        self.draw_time_plus =0.001
        self.draw_sign = 0
        self.monster_bird_blue = None
        if self.monster_bird_blue ==None:
            cho = random.randint(1,4)
            if cho ==1 :
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_red.png')
            elif cho ==2:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_yellow.png')
            elif cho ==3:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_blue.png')
            elif cho ==4:
                self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_green.png')

        self.bullet = Monster_bullet()

    def set_monster_bird_red(self):
        global choice
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_red.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_yellow(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time =random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_yellow.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_green(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_green.png')
        self.bullet = Monster_bullet()

    def set_monster_bird_blue(self):
        self.x = game_framework.ground_size_w + 50
        self.y = random.randint(1,18)*50
        self.speed = 3
        self.frame = 1
        self.draw_time = random.randint(1,499)*0.01
        self.bullet_time = 0
        self.draw_sign = 0
        self.monster_bird_blue = load_image('resorce\\monster\\monster_bird_blue.png')
        self.bullet = Monster_bullet()

    def draw(self):
        if self.draw_sign ==1:

            self.frame = (self.frame + 1) % 1
            self.monster_bird_blue.clip_draw(self.frame*36,0,36,42,self.x,self.y,60,60)
            self.bullet.draw()
            if(self.bullet_time>3):
                self.bullet.xy.append([self.x, self.y])
                self.bullet_time =0


    def update(self):
        global choice
        self.draw_time +=0.01
        self.bullet_time+=0.01
        if self.draw_time>5:
            self.x -= self.speed
            self.draw_sign=1
            self.bullet_time += 0.01
            self.bullet.update()
            if self.x < 0:
                if(choice == 1):
                    self.set_monster_bird_green()
                elif choice ==2 :
                    self.set_monster_bird_blue()
                elif choice == 3:
                    self.set_monster_bird_red()
                elif choice == 4:
                    self.set_monster_bird_yellow()

class Monster_bullet:
    def __init__(self):
        global choice
        self.xy = []
        self.image_level_one = load_image('resorce\\monster\\monster_bullet_1.png')
        self.x = 0
        self.y = 0
        self.t =0
        self.speed =5
        self.target_x=0
        self.target_y=0
        self.bullet_type =1
        self.time =0

    def update(self):
        pass

    def draw(self):
        if self.bullet_type ==1:
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    bxy[0] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0:
                        self.xy.remove(bxy)
        elif self.bullet_type ==2:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t ==1:
                    self.t=0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1-self.t)*bxy[0] + self.t*(-1200)
                    bxy[1] = (1-self.t)*bxy[1] + self.t*(200)
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] >600:
                        self.xy.remove(bxy)
        elif self.bullet_type == 3:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t == 1:
                    self.t = 0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1 - self.t) * bxy[0] + self.t * (-1200)
                    bxy[1] = (1 - self.t) * bxy[1] + self.t * (100)
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] > 600:
                        self.xy.remove(bxy)
        elif self.bullet_type == 4:
            if (len(self.xy) != 0):
                self.time += 0.1
                if self.time >= 3:
                    self.t += 0.005
                    self.time = 0
                if self.t == 1:
                    self.t = 0
                for i, bxy in enumerate(self.xy):
                    bxy[0] = (1 - self.t) * bxy[0] + self.t * (-1200)
                    bxy[1] = (1 - self.t) * bxy[1] + self.t * (400)
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 20, 20)
                    if bxy[0] <= 0 or bxy[1] > 600:
                        self.xy.remove(bxy)

        elif self.bullet_type == 5:  # 유도탄인데 아직 안된다
            if (len(self.xy) != 0):
                for i, bxy in enumerate(self.xy):
                    if self.target_x < self.x :
                        bxy[0] -= self.speed
                    if self.target_y < self.y :
                        bxy[1] -= self.speed
                    self.xy[i][0] = bxy[0]
                    self.image_level_one.clip_draw(0, 0, 20, 20, bxy[0], bxy[1], 30, 30)
                    if bxy[0] <= 0 or bxy[1] < 0:
                        self.xy.remove(bxy)

def enter():
    global kirby , back_ground , main_chracter_bullet
    global blue_monster,blue_monsters ,red_monster,red_monsters
    kirby = Kirby.Main_charcter()

    back_ground =Back_ground()
    main_chracter_bullet = Main_chracter_Bullet()
    blue_monster = Monster()
    blue_monsters = [Monster() for i in range(20)]
    red_monster = Monster()
    red_monsters = [Monster() for i in range(10)]





def exit():
    global kirby,back_ground ,main_chracter_bullet
    global blue_monster,blue_monsters,red_monster,red_monsters
    del (kirby)
    del (back_ground)
    del (main_chracter_bullet)
    del (blue_monster,blue_monsters)
    del (red_monster,red_monsters)

def pause():
    pass

def resume():
    pass

def handle_events():
    global kirby, back_ground, main_chracter_bullet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
#캐릭터 이동 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_x +=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_x -=1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            kirby.frame = (kirby.frame + 1) % 5
            kirby.dir_y -=1

        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            kirby.dir_x -=1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            kirby.dir_x += 1

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            kirby.dir_y -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            kirby.dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            main_chracter_bullet.power_level = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            main_chracter_bullet.power_level = 2

#총알 발사 구현
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            main_chracter_bullet.x = kirby.x
            main_chracter_bullet.y = kirby.y
            if(main_chracter_bullet.power_level==1):
                main_chracter_bullet.xy.append([main_chracter_bullet.x,main_chracter_bullet.y])
            elif(main_chracter_bullet.power_level==2):
                main_chracter_bullet.xy.append([main_chracter_bullet.x,main_chracter_bullet.y])
                main_chracter_bullet.xy_2.append([main_chracter_bullet.x, main_chracter_bullet.y])
                main_chracter_bullet.xy_2_2.append([main_chracter_bullet.x, main_chracter_bullet.y])

def update():
    global choice
    kirby.update()
    main_chracter_bullet.update()
    choice = random.randint(1,4)
    for blue_monster in blue_monsters:
        blue_monster.update()
    for red_monster in red_monsters:
        red_monster.update()




def draw():
    clear_canvas()
    back_ground.draw()
    kirby.draw()
    main_chracter_bullet.draw()
    for blue_monster in blue_monsters:
        blue_monster.draw()
    for red_monster in red_monsters:
        red_monster.draw()
    update_canvas()






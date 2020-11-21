import pygame
import load_resources as res
from game_action import quit_game
import random
from game_component import text_objects
from end_game import crashed
pygame.init()

score=0
def show_score(score):
    text_objects("Arial","Score: "+ str(score),30,res.white,100,50)


def road(y1,y2):
    y1=y1+5

    if y1>0:
        res.display_surface.blit(res.road_img,(0,y1))
        y2+=5.105
        res.display_surface.blit(res.road_img,(0,y2))

    if y1>590:
        y1=0
        y2=-590
    return y1,y2

def opponent(x,y,speed,img):
    global score
    res.display_surface.blit(img,(x,y))
    y+=speed

    if y>600:
        y=-200
        x=random.randrange(0,600)
        img=random.choice(res.opp_list)
        score=score+1
    return x,y,img






def game_window():
    global score
    running=True

    road_y1=0
    road_y2=-590

    car_x=400
    car_y=450

    x_change=0
    y_change=0

    opp_x1=random.randrange(0,600)
    opp_y1=-400
    opp_x2=random.randrange(0,600)
    opp_y2=-350
    opp_x3=random.randrange(0,600)
    opp_y3=-250

    img1=random.choice(res.opp_list)
    img2=random.choice(res.opp_list)
    img3=random.choice(res.opp_list)








    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit_game()


            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_UP:
                    y_change=-10
                elif event.key== pygame.K_DOWN:
                    y_change=10
                elif event.key== pygame.K_LEFT:
                    x_change=-10
                elif event.key== pygame.K_RIGHT:
                    x_change=10
            if event.type== pygame.KEYUP:
                if event.key==pygame.KEYUP or event.key==pygame.KEYDOWN or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                    y_change=0

        car_x+=x_change
        car_y+=y_change




        road_y1,road_y2=road(road_y1,road_y2)


        res.display_surface.blit(res.car_img,(car_x,car_y))
        opp_x1,opp_y1,img1=opponent(opp_x1,opp_y1,10,img1)
        opp_x2,opp_y2,img1=opponent(opp_x2,opp_y2,10,img1)
        opp_x3,opp_y3,img1=opponent(opp_x3,opp_y3,10,img1)
        
#crash
        car_width=res.car_img.get_size()[0]#(x,y)
        car_height=res.car_img.get_size()[1]

        opp_width=res.opp1_img.get_size()[0]#(x,y)
        opp_height=res.opp1_img.get_size()[1]

        if car_y<opp_y1 +opp_height:
            if car_x<opp_x1+opp_width and car_x+car_width>opp_x1:
                crashed(score)

        if car_y<opp_y2 +opp_height:
            if car_x<opp_x2+opp_width and car_x+car_width>opp_x2:
                crashed(score)
        if car_y<opp_y3 +opp_height:
            if car_x<opp_x3+opp_width and car_x+car_width>opp_x3:
                crashed(score)

        show_score(score)
        
        




        pygame.display.update()
        res.clock.tick(50)

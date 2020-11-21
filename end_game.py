import pygame
import load_resources as res
from game_component import text_objects,button
from game_action import quit_game
pygame.init()

def crashed(score):
    res.display_surface.blit(res.wall,(0,0))
    text_objects("Eras Demi ITC","YOU CRASHED!!" ,50,res.white,300,100)
    text_objects("Eras Demi ITC","Final Score:"+str(score) ,50,res.white,300,500)



    end=True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        pygame.display.update()

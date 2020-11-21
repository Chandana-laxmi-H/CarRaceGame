import pygame
from game_action import quit_game
import load_resources as res
from game_component import text_objects,button
from play_game import game_window
pygame.init()

def game_intro():
    start=True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        res.display_surface.blit(res.wall,(0,0))
        text_objects("Comic","LETS RACE",100,res.red,300,100)
        text_objects("Eras Demi ITC","Ready Steady Go",50,res.white,300,200)

        button("GO",res.red,100,50,100,500,game_window)
        button("QUIT",res.red,100,50,400,500,quit_game)

        pygame.display.update()

if __name__=='__main__':
    game_intro()

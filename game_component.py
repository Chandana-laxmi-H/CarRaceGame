import pygame
import load_resources as res
pygame.init()


def text_objects(font,text,size,color,x,y):
    my_font=pygame.font.SysFont(font,size)
    my_text=my_font.render(text,True,color)
    my_rect=my_text.get_rect(center=(x,y))
    res.display_surface.blit(my_text,my_rect)


def button(text,color,width,height,x,y,action=None):
    button_rect=pygame.draw.rect(res.display_surface,color,(x,y,width,height))
    text_objects("Comic",text,30,res.white,x+(width/2),y+(height/2))

    mouse_pos=pygame.mouse.get_pos() #x,y
    mouse_click=pygame.mouse.get_pressed() #(0,0,0)

#button pressed inside rect
    if button_rect.collidepoint(mouse_pos[0],mouse_pos[1]):
        if mouse_click[0]==1 and action!=None:
            action()




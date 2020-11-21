import pygame 

pygame.init()

clock=pygame.time.Clock()

dwidth=590
dheight=590
display_surface=pygame.display.set_mode((dwidth,dheight))
pygame.display.set_caption("2D Car Game")

car_img=pygame.image.load("resources/images/img1.jpeg")
oppcar_img=pygame.image.load("resources/images/img2.jpg")
road_img=pygame.image.load("resources/images/road.jfif")
wall=pygame.image.load("resources/images/wallpaper.jpg")

opp1_img=pygame.image.load("resources/images/opp1.jpeg")
opp2_img=pygame.image.load("resources/images/opp2.jpeg")

opp_list=[opp1_img,opp2_img]

#pygame.mixer.music.load("resources/sounds/bg_music.mp3")
#pygame.mixer.Sound("resources/sounds/crash.wav")

#colors

red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,250,0)
black=(0,0,0)



import pygame
from sys import exit

#Initalizing the programm
pygame.init()

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
font = pygame.font.Font("mypygame/font/Pixeltype.ttf", 50)

pygame.display.set_caption("Dr Traphouse")

#Surfaces
sky_surface = pygame.image.load("mypygame/graphics/sky.jpg").convert() #length of the surface
ground_surface = pygame.image.load("mypygame/graphics/ground.jpg").convert()

text_surface = font.render("H.A.U.", False, "Orange")

dog_surface = pygame.image.load("mypygame/graphics/piesek.png").convert_alpha()
dog_rectangle = dog_surface.get_rect(bottomleft = (20, 500))

player_surface = pygame.image.load("mypygame/graphics/belmondawg.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (700,500))


#Dane

if_player_collide_dog = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Background
    screen.blit(sky_surface, (0,-100)) #coordinates of the surface
    screen.blit(ground_surface, (0,500))

    #Title
    screen.blit(text_surface, (450, 100))

    #Dog
    dog_rectangle.x += 3
    if dog_rectangle.left > 1200:
        dog_rectangle.right = -100
    screen.blit(dog_surface,dog_rectangle)
    
    #Player
    screen.blit(player_surface,player_rectangle)

    if player_rectangle.colliderect(dog_rectangle) and if_player_collide_dog == False:
        if_player_collide_dog = True
        print(if_player_collide_dog)


    #Mouse
    mouse_position = pygame.mouse.get_pos()
    if player_rectangle.collidepoint(mouse_position):
        print("HEHE to bestseller")


    #refreshing the display
    pygame.display.update()
    clock.tick(60)
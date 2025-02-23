import pygame
pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#background image
background_img = pygame.image.load('background.png').convert_alpha()
#panel image
panel_img = pygame.image.load('panel.png').convert_alpha()

#function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))

#function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))

run = True
while run:

    clock.tick(fps)

    #draw background
    draw_bg()
    #draw panel
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
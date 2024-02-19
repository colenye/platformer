import pygame
import images
from sys import exit
pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
display = pygame.display.set_mode(resolution)

# === LOAD IMAGES === #
mario = pygame.image.load('Sprites/mario.png')

pygame.display.set_caption("Better platformer than the shawt")
pygame.display.set_icon(images.Images.mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)
import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=900.500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
BULLET_HIT_SOUND=pygame.mixer.Sound("assets/grenade.mp3")
BULLET_FIRE_SOUND=pygame.mixer.Sound("assets/gun.mp3")

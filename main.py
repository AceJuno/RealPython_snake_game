# This is main.py - It is responsible for initializing pygame and GameEngine
import pygame
import sys
import time
import engine

stop_time = time.monotonic()
start_time = 0
size = width, height = 1202, 794

pygame.init()
screen = pygame.display.set_mode(size)
game_engine = engine.Engine(screen)
game_engine.backsetup()

# main infinite loop used to update screen and call engine functions
while 1:
    game_engine.registermove()
    start_time = time.monotonic()

    if start_time - stop_time >= 0.3:
        stop_time = time.monotonic()

        game_engine.backsetup()
        game_engine.snakemove()

        if game_engine.collisiondetection():
            sys.exit()

    pygame.display.flip()

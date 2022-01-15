import pygame
import grid

width, height = 800, 600
size = (width, height)

pygame.init()
pygame.display.set_caption("What kind of life are we, no one will heal us")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
white = (255, 255, 255)
custom_color = (14, 88, 228)

scaler = 25
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.generate_array()

while True:
    clock.tick(fps)
    screen.fill(black)

    Grid.Conway(off_color=white, on_color=custom_color, surface=screen)

    pygame.display.update()


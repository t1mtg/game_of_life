import pygame
import numpy as np
import cell
from random import choice


class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height / scale)
        self.rows = int(width / scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size, dtype=np.object0)
        self.offset = offset

    def generate_array(self):
        seq = [cell.State.DEAD, cell.State.ALIVE]
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = choice(seq)

    def Conway(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                _x = 1 if x == cell.State.ALIVE else 0
                _y = 1 if y == cell.State.ALIVE else 0
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == cell.State.ALIVE:
                    pygame.draw.rect(surface, on_color,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(surface, off_color,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

        next_iteration = np.ndarray(shape=self.size, dtype=np.object0)

        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = cell.Cell.get_neighbours(cell.Cell(self), x, y)
                if state == cell.State.DEAD and neighbours == 3:
                    next_iteration[x][y] = cell.State.ALIVE
                elif state == cell.State.ALIVE and (neighbours < 2 or neighbours > 3):
                    next_iteration[x][y] = cell.State.DEAD
                else:
                    next_iteration[x][y] = state
        self.grid_array = next_iteration

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_array(self):
        return self.grid_array

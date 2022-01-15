from enum import Enum
import grid


class State(Enum):
    DEAD = 0
    ALIVE = 1


class Cell(object):
    def __init__(self, grid):
        self.grid = grid
        self.__state = State.DEAD
        self.__rows = grid.get_rows()
        self.__columns = grid.get_columns()
        self.__grid_array = grid.get_array()

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + self.__rows) % self.__rows
                y_edge = (y + m + self.__columns) % self.__columns
                if self.__grid_array[x_edge][y_edge] == State.ALIVE:
                    total += 1
        if self.__grid_array[x][y] == State.ALIVE:
            total -= 1
        return total

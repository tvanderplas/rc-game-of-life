
from itertools import product
'''
Game of Life
0-1 death
2 life
3 birth
4-8 death
'''

class Life:

    def __init__(self, size=(10, 10)):
        self.board = [[' ' for x in range(size[0])] for y in range(size[1])]
        self.size = size
        print('\n'.join([str(row) for row in self.board]))


    def neighbors(self, x, y):
        x_range = range(max(x - 1, 0), min(x + 2, self.size[0]))
        y_range = range(max(y - 1, 0), min(y + 2, self.size[1]))
        return [i for i in product(x_range, y_range) if i != (x, y)]


    def status(self, x, y, neighbors):
        living_neighbors = len([i for i in self.neighbors(x, y) if i == '#'])
        if living_neighbors == 3:
            return '#'
        else:
            return ' '


if __name__ == '__main__':
    pass


from itertools import product
'''
Game of Life
0-1 death
2 life
3 birth
4-8 death
'''

class Life:

    def __init__(self):
        self.board = [[' ' for x in range(10)] for y in range(10)]
        print('\n'.join([str(row) for row in self.board]))


    def neighbors(self, x, y):
        x_range = range(max(x - 1, 0), min(x + 2, 10))
        y_range = range(max(y - 1, 0), min(y + 2, 10))
        return [i for i in product(x_range, y_range) if i != (x, y)]


    def status(self, x, y, neighbors):
        living_neighbors = len([i for i in self.neighbors(x, y) if i == '#'])
        if living_neighbors == 3:
            return '#'
        else:
            return ' '


if __name__ == '__main__':
    pass

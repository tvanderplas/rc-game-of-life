
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
        
        
    def __str__(self):
        return '\n'.join([str(row) for row in self.board])


    def neighbors(self, x, y):
        x_range = range(max(x - 1, 0), min(x + 2, self.size[0]))
        y_range = range(max(y - 1, 0), min(y + 2, self.size[1]))
        return [(xx, yy) for (xx, yy) in product(x_range, y_range) if (xx, yy) != (x, y)]
    
    
    def status(self, x, y):
        living_neighbors = sum((1 for (xx, yy) in self.neighbors(x, y) if self.board[xx][yy] == '#'))
        if living_neighbors == 3:
            return '#'
        else:
            return ' '


if __name__ == '__main__':
    pass

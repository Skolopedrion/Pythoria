import random

from tile import Tile

N, S, E, W = 0b0001, 0b0010, 0b0100, 0b1000

WALL, EMPTY = Tile('█', True, True, False), Tile(' ', False, False, False)

intersection = {
    N | S | E | W: '\u253c',
    N | S | E: '\u251c',
    N | S | W: '\u2524',
    S | E | W: '\u252c',
    N | E | W: '\u2534',
    N | S: '\u2502',
    E | W: '\u2500',
    S | E: '\u250c',
    N | E: '\u2514',
    S | W: '\u2510',
    N | W: '\u2518',
    N: '\u2502',
    S: '\u2502',
    E: '\u2500',
    W: '\u2500',
    0: ' '
}

OPPOSITE = {
    N: S,
    S: N,
    E: W,
    W: E
}

class MazeCell:
    def __init__(self, fill, x, y):
        self.fill = fill
        self.x, self.y = x, y
        self.is_intact = True
        self.connection = {direction: True for direction in (N, S, E, W)}

    def between(self, other):
        if other.y < self.y:
            return N
        elif other.y > self.y:
            return S
        elif other.x > self.x:
            return E
        elif other.x < self.x:
            return W
        else:
            raise ValueError("'other' is not next to the cell.")

    def connect(self, other):
        self.is_intact, other.is_intact = False, False

        self.connection[self.between(other)] = False
        other.connection[OPPOSITE[self.between(other)]] = False

    def coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return "<MazeCell on ({x}, {y})>".format(
            x=self.x, y=self.y
        )

    def __bool__(self):
        return self.fill


class Maze(list):
    def __init__(self, width, height):
        self.width, self.height = width//2, height//2
        maze = [[MazeCell(True, ix, iy) for ix in range(self.width)]
                                        for iy in range(self.height)]
        super(Maze, self).__init__(maze)

        cells = []
        current = self.random_cell()
        visited = 1

        while visited < (self.height * self.width):
            intact = [c for c in self.neighbors(current) if c.is_intact]
            if intact:
                cell = random.choice(intact)
                current.connect(cell)
                cells.append(current)
                current = cell
                visited += 1

            else:
                current = cells.pop()

        cell_matrix = [[MazeCell(True, x, y) for x in range(self.width * 2 + 1)] for y in range(self.height * 2 + 1)]
        cell_stack = [self[x, y] for y in range(self.height) for x in range(self.width)]
        for cell in cell_stack:
            x = cell.x * 2 + 1
            y = cell.y * 2 + 1
            cell_matrix[y][x] = MazeCell(False, x, y)

            if not cell.connection[N] and y > 0:
                cell_matrix[y - 1][x] = MazeCell(False, x, y-1)
            if not cell.connection[S] and y + 1 < self.height:
                cell_matrix[y + 1][x] = MazeCell(False, x, y+1)
            if not cell.connection[E] and x + 1 < self.width:
                cell_matrix[y][x + 1] = MazeCell(False, x+1, y)
            if not cell.connection[W] and x > 0:
                cell_matrix[y][x - 1] = MazeCell(False, x-1, y)

        super(Maze, self).__init__(cell_matrix)

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            x, y = index
            self[y][x] = value
        else:
            return super().__setitem__(index, value)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            x, y = index
            return self[y][x]
        else:
            return super().__getitem__(index)

    def __repr__(self):
        display = ''
        for line in self:
            for cell in line:
                display += str(WALL if cell else EMPTY)
            display += '\n'
        return display

    def as_list(self):
        def str_cell(c):
            conns = 0b0000
            for i, neighbor in enumerate(self.neighbors(c, keep_position=True)):
                conns |= bool(neighbor) and bool(c) * (N, S, E, W)[i]
            return intersection[conns]

        lst = []
        for row in self:
            line = []
            for block in row:
                line.append(Tile(str_cell(block), True, True, False) if block else EMPTY)
            lst.append(line)
        return lst

    def neighbors(self, cell, keep_position=False):
        x, y = cell.x, cell.y
        n = []
        for new_x, new_y in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
            try:
                if (new_x < 0) or (new_y < 0):
                    raise IndexError
                n.append(self[new_x, new_y])
            except IndexError:
                if keep_position:
                    n.append(None)
        return n

    def random_cell(self, exclude_borders=False):
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        while len(self.neighbors(self[x, y])) < 4 and exclude_borders:
            x = random.randrange(self.width)
            y = random.randrange(self.height)
        return self[x, y]
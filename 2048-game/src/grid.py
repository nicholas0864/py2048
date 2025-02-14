class Grid:
    def __init__(self):
        self.size = 4
        self.grid = [[0] * self.size for _ in range(self.size)]

    def add_tile(self):
        import random
        empty_tiles = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def move_left(self):
        for row in self.grid:
            self._merge(row)

    def move_right(self):
        for row in self.grid:
            row.reverse()
            self._merge(row)
            row.reverse()

    def move_up(self):
        for c in range(self.size):
            col = [self.grid[r][c] for r in range(self.size)]
            self._merge(col)
            for r in range(self.size):
                self.grid[r][c] = col[r]

    def move_down(self):
        for c in range(self.size):
            col = [self.grid[r][c] for r in range(self.size)]
            col.reverse()
            self._merge(col)
            col.reverse()
            for r in range(self.size):
                self.grid[r][c] = col[r]

    def _merge(self, row):
        new_row = [i for i in row if i != 0]
        merged_row = []
        skip = False
        for i in range(len(new_row)):
            if skip:
                skip = False
                continue
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                merged_row.append(new_row[i] * 2)
                skip = True
            else:
                merged_row.append(new_row[i])
        merged_row += [0] * (self.size - len(merged_row))
        for i in range(self.size):
            row[i] = merged_row[i]

    def can_move(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return True
                if j < self.size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return True
                if i < self.size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return True
        return False

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.grid])
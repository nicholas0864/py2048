from grid import Grid
import pygame

class Game:
    def __init__(self):
        self.score = 0
        self.grid = Grid()
        self.grid.add_tile()
        self.grid.add_tile()

    def move_up(self):
        self.grid.move_up()
        self.grid.add_tile()

    def move_down(self):
        self.grid.move_down()
        self.grid.add_tile()

    def move_left(self):
        self.grid.move_left()
        self.grid.add_tile()

    def move_right(self):
        self.grid.move_right()
        self.grid.add_tile()

    def update(self):
        if not self.grid.can_move():
            print("Game Over!")
            self.reset()

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }
        for r in range(4):
            for c in range(4):
                value = self.grid.grid[r][c]
                color = colors.get(value, (60, 58, 50))
                pygame.draw.rect(screen, color, (c * 180 + 10, r * 180 + 10, 160, 160))
                if value != 0:
                    text = font.render(str(value), True, (255, 255, 255))
                    text_rect = text.get_rect(center=(c * 180 + 90, r * 180 + 90))
                    screen.blit(text, text_rect)

    def reset(self):
        self.score = 0
        self.grid = Grid()
        self.grid.add_tile()
        self.grid.add_tile()
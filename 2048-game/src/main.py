import pygame
from game import Game

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

# Initialize the game
game = Game()

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle key presses for game controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.move_up()
            elif event.key == pygame.K_DOWN:
                game.move_down()
            elif event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()

    # Update the game state
    game.update()

    # Draw the game
    screen.fill("brown")
    game.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
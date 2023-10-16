import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.start_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    game.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction("RIGHT")
                elif event.key == pygame.K_SPACE:
                    game.pause_game()

        game.update()
        game.draw()

if __name__ == "__main__":
    main()

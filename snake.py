import pygame, random

pygame.init()
win = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
snake_block = 10

def gameLoop():
    game_over = False
    x, y = 200, 200
    dx, dy = 0, 0
    snake = [[x, y]]
    length = 1
    food_x = round(random.randrange(0, 400 - snake_block) / 10) * 10
    food_y = round(random.randrange(0, 400 - snake_block) / 10) * 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy

        if x >= 400 or x < 0 or y >= 400 or y < 0:
            game_over = True

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (food_x, food_y, snake_block, snake_block))

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for segment in snake:
            pygame.draw.rect(win, (0, 255, 0), (segment[0], segment[1], snake_block, snake_block))

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, 400 - snake_block) / 10) * 10
            food_y = round(random.randrange(0, 400 - snake_block) / 10) * 10
            length += 1

        pygame.display.update()
        clock.tick(15)

    pygame.quit()

gameLoop()

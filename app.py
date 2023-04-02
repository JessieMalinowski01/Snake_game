import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 25)

# Set up the snake
snake_block_size = 10
snake_speed = 15


def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(
            screen, black, [x[0], x[1], snake_block_size, snake_block_size])

# Set up the game loop
def game_loop():
    game_over = False
    game_close = False

    # Set up the initial position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Set up the change in position of the snake
    x1_change = 0
    y1_change = 0

    # Set up the length of the snake
    snake_list = []
    length_of_snake = 1

    # Set up the initial position of the food
    foodx = round(random.randrange(
        0, screen_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(
        0, screen_height - snake_block_size) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Game over screen
        while game_close == True:
            screen.fill(white)
            game_over_text = font.render(
                "Game Over, Press Q-Quit or C-Play Again", True, black)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (screen_width / 2, screen_height / 2)
            screen.blit(game_over_text, game_over_rect)

            # Update the display
            pygame.display.update()

            # Handle key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

                # Check if the snake hits the wall
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Fill the screen with white color
        screen.fill(white)

        # Draw the food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block_size, snake_block_size])

        # Update the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        snake(snake_block_size, snake_list)

        # Update the length of the snake if it eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
            length_of_snake += 1

        # Update the display
        pygame.display.update()

        # Set up the game clock
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()

    # Quit Python
    quit()

# Start the game loop
game_loop()

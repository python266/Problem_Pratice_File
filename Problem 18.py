import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load images
background_img = pygame.image.load("assets/background.png").convert()
bird_img = pygame.image.load("assets/bird.png").convert_alpha()
pipe_img = pygame.image.load("assets/pipe.png").convert_alpha()

# Set up the bird
bird_x = 50
bird_y = 200
bird_speed = 0
bird_acceleration = 0.5
bird_max_speed = 10
bird_rect = bird_img.get_rect()

# Set up the pipes
pipe_width = 52
pipe_gap = 100
pipe_speed = 3
pipe_list = []

# Set up the game loop
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    # Move the bird
    bird_speed += bird_acceleration
    if bird_speed > bird_max_speed:
        bird_speed = bird_max_speed
    bird_y += bird_speed
    bird_rect.center = (bird_x, bird_y)

    # Move the pipes
    for pipe in pipe_list:
        pipe[0] -= pipe_speed
    if pipe_list and pipe_list[0][0] < -pipe_width:
        pipe_list.pop(0)
    if len(pipe_list) < 3:
        pipe_list.append([screen_width, random.randint(50, 350)])

    # Draw the background and pipes
    screen.blit(background_img, (0, 0))
    for pipe in pipe_list:
        screen.blit(pipe_img, (pipe[0], pipe[1] - pipe_img.get_height() - pipe_gap))
        screen.blit(pipe_img, (pipe[0], pipe[1] + pipe_gap))

    # Draw the bird
    screen.blit(bird_img, bird_rect)

    # Check for collisions
    for pipe in pipe_list:
        pipe_rect = pygame.Rect(pipe[0], pipe[1] - pipe_img.get_height() - pipe_gap, pipe_width, pipe_img.get_height())
        if bird_rect.colliderect(pipe_rect) or bird_rect.top < 0 or bird_rect.bottom > screen_height:
            running = False

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
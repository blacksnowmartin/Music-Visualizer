import pygame
import sys
import math
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Visualizer - Spiraling Flowers")

# Set up colors
background_color = (255, 255, 255)  # White
flower_color = (255, 0, 0)          # Red

# Set up flower variables
flower_radius = 10
num_flowers = 50
flower_positions = []

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Generate random flower positions
    if len(flower_positions) < num_flowers:
        x = random.randint(flower_radius, width - flower_radius)
        y = random.randint(flower_radius, height - flower_radius)
        flower_positions.append((x, y))

    # Draw the scene
    screen.fill(background_color)

    for x, y in flower_positions:
        pygame.draw.circle(screen, flower_color, (x, y), flower_radius)
        flower_radius += 1

    pygame.display.flip()
    clock.tick(60)

import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Qatar World Cup Visualizer")

# Set up colors
background_color = (255, 255, 204)  # Light Yellow
desert_color = (244, 164, 96)        # Sandy Brown
mascot_color = (255, 69, 0)          # Red-Orange

# Set up mascot variables
mascot_size = 50
mascot_jump = 0
mascot_y = height - mascot_size

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update mascot jump
    if random.randint(0, 100) == 0:
        mascot_jump = 10

    mascot_jump = max(0, mascot_jump - 1)

    # Draw the scene
    screen.fill(background_color)

    # Draw desert
    pygame.draw.rect(screen, desert_color, (0, height // 2, width, height // 2))

    # Draw sun
    pygame.draw.circle(screen, (255, 255, 0), (width - 50, 50), 30)

    # Draw World Cup mascot (simplified representation)
    pygame.draw.rect(screen, mascot_color, (width // 2 - mascot_size // 2, mascot_y - mascot_jump, mascot_size, mascot_size))

    pygame.display.flip()
    clock.tick(60)

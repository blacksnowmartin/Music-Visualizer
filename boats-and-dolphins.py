import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boat and Dolphin Visualizer")

# Set up colors
background_color = (135, 206, 250)  # Sky Blue
sea_color = (0, 119, 190)            # Deep Sky Blue
boat_color = (139, 69, 19)           # Saddle Brown
dolphin_color = (70, 130, 180)       # Steel Blue

# Set up boat variables
boat_width, boat_height = 80, 40
sea_level = 100
boat_speed = 2
boats = []

# Set up dolphin variables
dolphin_size = 30
dolphin_jump = 0
dolphins = []

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move boats and create new ones
    for boat in boats:
        boat[0] -= boat_speed
        if boat[0] + boat_width < 0:
            boats.remove(boat)

    if random.randint(0, 30) == 0:
        boat_x = width
        boat_y = height - sea_level - boat_height
        boats.append([boat_x, boat_y])

    # Move dolphins and create new ones
    for dolphin in dolphins:
        dolphin[0] -= boat_speed
        dolphin[1] = height - sea_level - dolphin_size - dolphin_jump

    if random.randint(0, 100) == 0:
        dolphin_x = width
        dolphin_y = height - sea_level - dolphin_size
        dolphins.append([dolphin_x, dolphin_y])

    # Update dolphin jump
    dolphin_jump = max(0, dolphin_jump - 1)

    # Draw the scene
    screen.fill(background_color)

    # Draw sea
    pygame.draw.rect(screen, sea_color, (0, height - sea_level, width, sea_level))

    # Draw boats
    for boat in boats:
        pygame.draw.rect(screen, boat_color, (boat[0], boat[1], boat_width, boat_height))

    # Draw dolphins
    for dolphin in dolphins:
        pygame.draw.circle(screen, dolphin_color, (dolphin[0], dolphin[1] - dolphin_jump), dolphin_size)

    pygame.display.flip()
    clock.tick(60)

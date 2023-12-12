import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minecraft Car Visualizer")

# Set up colors
background_color = (135, 206, 250)  # Sky Blue
road_color = (105, 105, 105)        # Dim Gray
car_color = (255, 0, 0)             # Red

# Set up car variables
car_width, car_height = 30, 20
road_height = 100
car_speed = 5
cars = []

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move cars and create new ones
    for car in cars:
        car[1] += car_speed
        if car[1] > height:
            cars.remove(car)

    if random.randint(0, 10) == 0:
        car_x = random.randint(0, width - car_width)
        car_y = 0 - car_height
        cars.append([car_x, car_y])

    # Draw the scene
    screen.fill(background_color)

    # Draw road
    pygame.draw.rect(screen, road_color, (0, height - road_height, width, road_height))

    # Draw cars
    for car in cars:
        pygame.draw.rect(screen, car_color, (car[0], car[1], car_width, car_height))

    pygame.display.flip()
    clock.tick(60)

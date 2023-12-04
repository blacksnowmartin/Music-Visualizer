import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Visualization - Digit 8")

# Set up font
font = pygame.font.SysFont("Arial", 48)

# Function to create a popping 8
def create_popping_8():
    x = random.randint(0, width)
    y = random.randint(0, height)
    return {"text": "8", "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            "position": [x, y], "velocity": [random.randint(-5, 5), random.randint(-5, 5)]}

# Main loop
clock = pygame.time.Clock()
digits = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add new 8s randomly
    if random.random() < 0.1:
        digits.append(create_popping_8())

    # Update 8 positions and remove off-screen ones
    for digit in digits:
        digit["position"][0] += digit["velocity"][0]
        digit["position"][1] += digit["velocity"][1]

    digits = [digit for digit in digits if 0 <= digit["position"][0] <= width and 0 <= digit["position"][1] <= height]

    # Draw the screen
    screen.fill((0, 0, 0))
    for digit in digits:
        text = font.render(digit["text"], True, digit["color"])
        screen.blit(text, digit["position"])

    pygame.display.flip()
    clock.tick(60)

import random
import math
import pygame

pygame.init()

# Display
width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monte Carlo Simulation")

# Variables
radius = width // 2
center = (width // 2, height // 2)
inside_circle = 0
total_points = 0

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

def draw_circle():
    pygame.draw.circle(win, white, center, radius, 1)


def draw_point(x, y, color):
    pygame.draw.circle(win, color, (x, y), 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    # random points
    x = random.randint(0, width)
    y = random.randint(0, height)
    distance = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)

    if distance <= radius:
        inside_circle += 1
        color = blue
    else:
        color = red

    total_points += 1

    draw_point(x, y, color)

    # Estimate π
    pi_estimate = 4 * inside_circle / total_points
    # circle = πr^2, square = 4r^2
    # π = 4 * (circle / square)

    pygame.display.update()
    if total_points % 1000 == 0:
        print(f"Total Points: {total_points}, π Estimate: {pi_estimate}")

    pygame.time.delay(1)

pygame.quit()

import pygame
import math

# Initialize Pygame
pygame.init()

# Constants for display
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
GREEN = (180,22,0)
# Planet class
class Planet:
    def __init__(self, name, radius, distance, color, angle_speed):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color
        self.angle = 0
        self.angle_speed = angle_speed

    def update(self):
        self.angle += self.angle_speed

    def draw(self):
        x = WIDTH // 2 + self.distance * math.cos(self.angle)
        y = HEIGHT // 2 + self.distance * math.sin(self.angle)
        pygame.draw.circle(SCREEN, self.color, (int(x), int(y)), self.radius)

# Create planets
sun = Planet("Sun", 50, 0, YELLOW, 0)
mercury = Planet("Mercury", 5, 100, GRAY, 0.3)
venus = Planet("Venus", 10, 150, RED, 0.02)
earth = Planet("Earth", 12, 200, BLUE, 0.15)
jupiter = Planet("Jupiter",22,240,GREEN,0.16)
planets = [mercury, venus, earth]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(WHITE)
    
    sun.draw()

    for planet in planets:
        planet.update()
        planet.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


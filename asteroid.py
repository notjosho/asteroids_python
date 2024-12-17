from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, RED
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, RED, self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    random_angle = random.uniform(20, 50)
    first = self.velocity.rotate(random_angle)
    second = self.velocity.rotate(-random_angle)

    new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
    self.first_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
    self.second_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

    self.first_asteroid.velocity = pygame.Vector2(first) * 1.2
    self.second_asteroid.velocity = pygame.Vector2(second) * 1.2

    self.kill()

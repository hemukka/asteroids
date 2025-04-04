import pygame
import random
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid
        self.position += self.velocity * dt
        
        # Check if it's far enough off-screen to be removed
        # Use the radius as a margin so we don't remove asteroids too early
        margin = self.radius * 2
        if (self.position.x < -margin or 
            self.position.x > SCREEN_WIDTH + margin or
            self.position.y < -margin or
            self.position.y > SCREEN_HEIGHT + margin):
            self.kill()

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            #return not None to indicate asteroid was killed, for stats
            return 1
        
        random_angle = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(random_angle)
        new_direction_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_direction_1 * 1.2
        new_asteroid_2.velocity = new_direction_2 * 1.2
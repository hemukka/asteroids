import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        # Move the shot
        self.position += self.velocity * dt
        
        # Check if it's far enough off-screen to be removed
        # Use the radius as a margin so we don't remove asteroids too early
        margin = self.radius * 2
        if (self.position.x < -margin or 
            self.position.x > SCREEN_WIDTH + margin or
            self.position.y < -margin or
            self.position.y > SCREEN_HEIGHT + margin):
            self.kill()
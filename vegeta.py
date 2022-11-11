import pygame
from pygame.sprite import Sprite


class Vegeta(Sprite):

    def __init__(self, alien_invasion_game):
        super().__init__()
        """Initialize the ship and set its starting position"""
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('vegeta.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)


    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.settings.vegeta_speed * self.settings.fleet_direction)
        self.rect.x = self.x

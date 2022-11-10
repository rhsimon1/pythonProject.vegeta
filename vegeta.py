import pygame
from pygame.sprite import Sprite


class Vegeta(Sprite):

    def __init__(self, alien_invasion_game):
        super().__init__()
        """Initialize the ship and set its starting position"""
        self.screen = alien_invasion_game.screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('vegeta.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

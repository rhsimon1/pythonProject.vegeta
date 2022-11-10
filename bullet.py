import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set the correct position.
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        print("made it here")
        self.bullet_rect.midtop = ai_game.goku_ai.goku_rect.midtop
        print('stopped here')
        # Store the bullet's postion as a decimal value.
        self.y = float(self.bullet_rect.y)
        print('fired')

    #This is a method from the SPRITE class
    def update(self):
        print('were here now')
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.bullet_rect.y = self.y
        print('done with this')


    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

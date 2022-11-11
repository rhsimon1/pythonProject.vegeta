import pygame


class Goku():
    """A class to manage Goku"""
    def __init__(self, alien_invasion_game):
        """Initialize the ship and set its starting position"""
        self.screen = alien_invasion_game.screen
        # Get the rect of alien invasion so that you can assign to the image
        self.screen_rect = alien_invasion_game.screen.get_rect()

        self.settings = alien_invasion_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('goku_resize.bmp')
        self.rect = self.image.get_rect()

        # Make a variable equal to Alien Invasion rectangle so that we can place the image rectangle on it.
        # Place the image at the midbottom
        # insure this variable comes before x and y value since this is the starting position
        self.rect.midbottom = self.screen_rect.midbottom


        # Assign x to self.goku_rect.x value as a float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Assign movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.goku_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.goku_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.goku_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.goku_speed

        # Assign the images rect x and y to the updated x and y values with the speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)

    def center_goku(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
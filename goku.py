import pygame


class Goku():
    """A class to manage Goku"""
    def __init__(self, alien_invasion_game):
        """Initialize the ship and set its starting position"""
        self.screen = alien_invasion_game.screen
        # Get the rect of alien invasion so that you can assign to the image
        self.screen_rect = alien_invasion_game.screen.get_rect()
        print(self.screen_rect.right)
        print(self.screen_rect.left)
        self.settings = alien_invasion_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('goku_resize.bmp')
        self.goku_rect = self.image.get_rect()

        # Make a variable equal to Alien Invasion rectangle so that we can place the image rectangle on it.
        # Place the image at the midbottom
        # insure this variable comes before x and y value since this is the starting position
        self.goku_rect.midbottom = self.screen_rect.midbottom
        print('1. Displaying Goku midbottom')
        print(self.goku_rect)

        # Assign x to self.goku_rect.x value as a float
        self.x = float(self.goku_rect.x)
        print('2.Displaying x float')
        self.y = float(self.goku_rect.y)
        print('3.Displaying y float')

        print(self.goku_rect)

        # Assign movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_movement(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right and self.goku_rect.right < self.screen_rect.right:
            self.x += self.settings.goku_speed
        if self.moving_left and self.goku_rect.left > 0:
            self.x -= self.settings.goku_speed
        if self.moving_up and self.goku_rect.top > 0:
            self.y -= self.settings.goku_speed
        if self.moving_down and self.goku_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.goku_speed

        # Assign the images rect x and y to the updated x and y values with the speed
        self.goku_rect.x = self.x
        self.goku_rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        print('Displaying goku using blit')
        self.screen.blit(self.image, self.goku_rect)

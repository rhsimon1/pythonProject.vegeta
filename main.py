import sys  # System-specific parameters and functions
import pygame  # Access Pygame functionality
from pygame import sprite
# import the class settings from the Settings file
# import the goku class from the Goku file
from goku import Goku
from bullet import Bullet
from settings import Settings
from vegeta import Vegeta


class AlienInvasion:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # init() is a method in pygame
        self.settings = Settings()   # Initialize the Setting class = self.settings so that we dont have all the settings in one file
        # This is how we change the resolution and the display. Display creates a surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")  # Set the display caption to Alien Invasion
        print('1. Displaying goku')
        self.goku_ai = Goku(self)
        self.bullets = pygame.sprite.Group()
        print('making a group')
        self.vegetas = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.

            self._check_events()

            # Update Goku image movement

            self.goku_ai.update_movement()

            # Update bullets with this method

            self._update_bullets()

            # Make the most recently drawn screen visible.

            self._update_screen()

    def _check_events(self):
        # This for loop checks every event.
        for event in pygame.event.get():
            # if the event is the quit type SYS will exit
            if event.type == pygame.QUIT:
                sys.exit()

            # this wil allow continues movement when pressing the right button
            # elif statement for when you press a button down
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events_(event)
            # elif statement for when you let go of they key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events_(event)

    def _check_keydown_events_(self, event):
        # Moves the image to the right
        if event.key == pygame.K_RIGHT:
            self.goku_ai.moving_right = True
        # Moves the image to the left
        elif event.key == pygame.K_LEFT:
            self.goku_ai.moving_left = True
        elif event.key == pygame.K_UP:
            self.goku_ai.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.goku_ai.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:

            self.__fire_bullet()

    def __fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events_(self, event):
        # Stops the image from moving
        if event.key == pygame.K_LEFT:
            self.goku_ai.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.goku_ai.moving_right = False
        elif event.key == pygame.K_UP:
            self.goku_ai.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.goku_ai.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.goku_ai.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.vegetas.draw(self.screen)

        pygame.display.flip()

    def _update_bullets(self):
        # Show bullets on screen
        print('Im here')
        self.bullets.update()
        print("second here")
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Make Vegeta.
        # Spacing between each Vegeta is equal to one vegeta width.

        vegeta = Vegeta(self)
        print('first math')
        vegeta_width, vegeta_height = vegeta.rect.size
        available_space_x = self.settings.screen_width - (vegeta_width)
        print(f'available space: {available_space_x} settings.screen_width: {self.settings.screen_width} - 2*vegeta_width: {2*vegeta_width}')
        number_vegeta_x = available_space_x // (2* vegeta_width)
        #Determine the number of rows of aliens that fit on the screen
        goku_height = self.goku_ai.goku_rect.height
        available_space_y = (self.settings.screen_height - (3*vegeta_height) - goku_height)
        number_rows = available_space_y // (2*goku_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for vegeta_number in range(number_vegeta_x):
                self._creat_alien(vegeta_number, row_number)

    def _creat_alien(self, vegeta_number, row_number):
        vegeta = Vegeta(self)
        vegeta_width, vegeta_height = vegeta.rect.size
        # vegeta_width doesn't change only vegeta_number changes after every iteration. vegeta_width/X coordinate is a constant.
        vegeta.x = vegeta_width + 2 * vegeta_width * vegeta_number
        vegeta.rect.x = vegeta.x
        vegeta.rect.y = vegeta_height + 2 * vegeta.rect.height * row_number
        self.vegetas.add(vegeta)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()





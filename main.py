import sys  # System-specific parameters and functions
import pygame  # Access Pygame functionality
# import the class settings from the Settings file
# import the goku class from the Goku file
from goku import Goku
from bullet import Bullet
from settings import Settings
from vegeta import Vegeta
from random import randint
from time import sleep
from gamestats import Gamestats
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
        self.goku_ai = Goku(self)
        self.stats = Gamestats(self)
        self.bullets = pygame.sprite.Group()
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

            self._update_vegetas()

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

    def _update_vegetas(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.vegetas.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.goku_ai, self.vegetas):
            self._goku_hit()
            print(self.stats.ships_left)

    def _update_bullets(self):
        # Show bullets on screen
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_vegeta_collison()
        # Check for any bullets that have collided with vegeta
        # If so, get rid of the bullet and vegeta

    def _check_bullet_vegeta_collison(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.vegetas, True, True)
        if not self.vegetas:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Make Vegeta.
        # Spacing between each Vegeta is equal to one vegeta width.
        #Create an instance of Vegeta with attributes of AI
        vegeta = Vegeta(self)
        # We need the width and height of an alien, so with this we use the attribute size, which contain a tuple
        # with the width and height of vegeta(object)
        vegeta_width, vegeta_height = vegeta.rect.size
        available_space_x = self.settings.screen_width - (vegeta_width)
        number_vegeta_x = available_space_x // (5* vegeta_width)

        #Determine the number of rows of aliens that fit on the screen
        goku_height = self.goku_ai.rect.height
        available_space_y = (self.settings.screen_height - (3*vegeta_height) - goku_height)
        number_rows = available_space_y // (5*goku_height)

        # Create the full fleet of aliens.

        for row_number in range(number_rows):
            for vegeta_number in range(number_vegeta_x):
                self._creat_alien(vegeta_number, row_number)

    def _creat_alien(self, vegeta_number, row_number):
        vegeta = Vegeta(self)
        vegeta_width, vegeta_height = vegeta.rect.size
        # vegeta_width doesn't change only vegeta_number changes after every iteration. vegeta_width/X coordinate is a constant.
        vegeta.x = vegeta_width + 2 * vegeta_width * vegeta_number
        vegeta.y = vegeta_height + 2 * vegeta.rect.height * row_number

        vegeta.rect.x = vegeta.x
        vegeta.rect.y = vegeta.y
        self.vegetas.add(vegeta)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""

        for vegeta in self.vegetas.sprites():
            if vegeta.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entrie fleet and change the fleet's direction."""
        for vegeta in self.vegetas.sprites():
            vegeta.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _goku_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        self.stats.ships_left -= 1
        # Get rid of any remaining vegeta and bullets
        self.vegetas.empty()
        self.bullets.empty()

        #Create a new fleet and center the ship.
        self._create_fleet()
        self.goku_ai.center_goku()

        # Pause
        sleep(0.5)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()





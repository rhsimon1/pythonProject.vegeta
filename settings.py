class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.goku_speed = 10
        # These are the Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 20
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.vegeta_speed = 5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


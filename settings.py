class Settings:
    # a class to store all settings for Alien Invasaion
    def __init__(self):
        # initialize the game's statis settings
        #Screen setting
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #scoring settings
        self.alien_points = 50

        # ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10


        # alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speed's up.
        self.speedup_scale = 1.1
        # How quickly the alien points increase in value
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


        
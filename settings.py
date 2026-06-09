class Settings:
    # a class to store all settings for Alien Invasaion
    def __init__(self):
        # initialize the game's settings
        #screen setting
        self.screen_width = 1366
        self.screen_height =700
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 6
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5


        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet _direction of 1 represents right; -1 represents left
        self.fleet_direction = 1


        
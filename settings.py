class Settings:
    # a class to store all settings for Alien Invasaion
    def __init__(self):
        # initialize the game's settings
        #screen setting
        self.screen_width = 850
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 5

        #bullet settings
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5


        
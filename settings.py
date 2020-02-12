class Settings:
    """
    Class to define game's settings
    """

    def __init__(self):
        """We initialize the game with some settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,255)
        # Bar settings
        self.bar_width = 150
        self.bar_speed = 7
        # Ball settings
        self.ball_pos_x = int(self.screen_width/2)
        self.ball_pos_y = int(self.screen_height/2)
        self.ball_speed = 10
        self.ball_radius = 15
        self.ball_color = (255,255,255)
        self.ball_left = 3
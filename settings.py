class Settings:
    """
    Class to define game's settings
    """

    def __init__(self):
        """We initialize the game with some settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,255)
        # Bar speed
        self.bar_speed = 2
        # Ball settings
        self.ball_speed = 3
        self.ball_radius = 15
        self.ball_color = (255,255,255)
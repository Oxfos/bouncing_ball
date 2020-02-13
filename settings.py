from time import perf_counter

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
        self.bar_speed = 8
        # Ball settings
        self.ball_pos_x = int(self.screen_width/2)
        self.ball_pos_y = int(self.screen_height/2)
        self.ball_start_angle = 15 # between 1 and 179
        self.ball_end_angle = 165 # between 1 and 179
        self.ball_speed = 3
        self.ball_radius = 15
        self.ball_color = (255,255,255)
        self.ball_left = 3
        # Game factors
        self.session_duration = 30
        self.difficulty_factor = 1.1

    def initialize_settings(self):
        """Initialize game difficulty parameters."""
        self.ball_radius = 15
        self.ball_speed = 3
        self.bar_width = 150

    def increase_game_difficulty(self):
        """Increase game difficulty."""
        self.ball_radius /= self.difficulty_factor
        self.ball_speed *= self.difficulty_factor
        self.bar_width /= self.difficulty_factor

    def time_elapsed(self, start):
        """Checks the elapsed time since start."""
        if perf_counter() - start == 30:
            return True
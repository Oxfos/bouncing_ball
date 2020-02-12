class GameStats:
    """Game statistics"""

    def __init__(self, bb_game):
        """Initialization of game statistics"""
        self.settings = bb_game.settings
        self.bounces = 0
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ball_left = self.settings.ball_left
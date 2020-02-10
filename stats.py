class GameStats:
    """Game statistics"""

    def __init__(self, bb_game):
        """Initialization of game statistics"""
        self.settings = bb_game.settings
        self.bounces = 0
        self.game_active = True
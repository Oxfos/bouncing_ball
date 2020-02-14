import pygame
from time import perf_counter

class TimeBar:
    """Time bar indicating remaining session time."""
    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.stats = bb_game.stats
        self.screen = bb_game.screen
        self.hight = self.settings.timebar_hight
        self.color = self.settings.timebar_color
        # Define timebar size, start position
        self.x = 10
        self.y = 10
        self.rect = pygame.Rect(self.x, self.y, self.settings.timebar_width,
             self.settings.timebar_hight)

    def update(self, game):
        #Updates the timebar length.
        session_time = game.settings.session_duration
        if perf_counter() - game.start_int >= session_time/100:
            game.start_int = perf_counter()
            game.timebar.rect.width -= self.settings.timebar_width/100
            print(game.timebar.rect.width)

    def reset_bar(self):
        self.rect.width = self.settings.timebar_width

    def draw_timebar(self):
        """Draws the time-bar."""
        pygame.draw.rect(self.screen, self.color, self.rect)
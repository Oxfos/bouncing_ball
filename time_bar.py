import pygame
from time import perf_counter

class TimeBar:
    """Time bar indicating remaining session time."""
    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.hight = self.settings.timebar_hight
        self.color = self.settings.timebar_color
        # Define timebar size, start position
        self.x = 10
        self.y = 10
        self.rect = pygame.Rect(self.x, self.y, self.settings.timebar_width,
             self.settings.timebar_hight)

    def update(self, bb_game):
        """Updates the timebar length every second."""
        session_time = self.settings.session_duration
        if perf_counter() - bb_game.start >= session_time/10:
            bb_game.timebar.rect.width -= self.settings.timebar_width/100

    def draw_timebar(self):
        """Draws the time-bar."""
        pygame.draw.rect(self.screen, self.color, self.rect)
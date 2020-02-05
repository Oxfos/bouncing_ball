import pygame

class Ball:
    """Class to model a bouncing ball"""

    def __init__(self, bb_game):
        """Initialize ball"""
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.color = self.settings.ball_color

        # Create ball at (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.ball_width,
            self.settings.ball_height)
        self.rect.center = bb_game.screen.center
        
        # Store ball's position as a decimal value
        self.x = float(self.rect.x)

    # Movement
    def update(self):
        self.x += self.settings.ball_speed
        self.rect.x = self.x

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
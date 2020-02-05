import pygame

class Ball:
    """Class to model a bouncing ball"""

    def __init__(self, bb_game):
        """Initialize ball"""
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.radius = self.settings.ball_radius
        self.color = self.settings.ball_color

        # Ball start position
        self.pos_x = int(self.settings.screen_width/2)
        self.pos_y = int(self.settings.screen_height/2)
        self.pos = (self.pos_x, self.pos_y)
        
        # Store ball's position as a decimal value
        # self.x = float(self.rect.x)

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, 
            self.pos, self.radius)
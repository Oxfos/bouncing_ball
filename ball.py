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
        self.old_x = self.pos_x
        
    def update(self):
        """Update x position"""
        if (self.pos_x - self.old_x) > 0:
            self.old_x = self.pos_x
            if self.pos_x < self.settings.screen_width:
                self.pos_x += int(self.settings.ball_speed)
            else:
                self.pos_x -= int(self.settings.ball_speed)
        else:
            self.old_x = self.pos_x
            if self.pos_x > 0:
                self.pos_x -= int(self.settings.ball_speed)
            else:
                self.pos_x += int(self.settings.ball_speed)
        

    def draw_ball(self):
        """Draw the ball on the screen"""
        pygame.draw.circle(self.screen, self.color, 
            (self.pos_x, self.pos_y), self.radius)
import pygame
from random import randint

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
    
        # initialize old position
        self.start = self.start()
        print(self.pos_x, self.pos_y)
        print(self.old_x, self.old_y)
        
    def start(self):
        """Function to get ball rolling randomly"""
        self.old_x = randint(self.pos_x-5, self.pos_x+5)
        self.old_y = randint(self.pos_y-5, self.pos_y+5)

    def update(self):
        """Update x position"""
        dist_x = self.pos_x - self.old_x
        dist_y = self.pos_y - self.old_y        
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        if dist_x > 0:
            if self.pos_x < self.settings.screen_width:
                self.pos_x += abs(dist_x)
            else:
                self.pos_x -= abs(dist_x)
        else:
            if self.pos_x > 0:
                self.pos_x -= abs(dist_x)
            else:
                self.pos_x += abs(dist_x)
        if dist_y < 0:
            if self.pos_y > 0:
                self.pos_y -= abs(dist_y)
            else:
                self.pos_y += abs(dist_y)
        else:
            if self.pos_y < self.settings.screen_height:
                self.pos_y += abs(dist_y)
            else:
                self.pos_y -= abs(dist_y)

        

    def draw_ball(self):
        """Draw the ball on the screen"""
        pygame.draw.circle(self.screen, self.color, 
            (self.pos_x, self.pos_y), self.radius)
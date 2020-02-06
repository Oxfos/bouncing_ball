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
        """Function to get ball rolling randomly upon initiation."""
        self.old_x = randint(self.pos_x-self.settings.ball_speed,
         self.pos_x+self.settings.ball_speed)
        self.old_y = randint(self.pos_y-self.settings.ball_speed,
         self.pos_y+self.settings.ball_speed)

    def update(self):
        """Updates ball position"""
        # Get difference between new and old position
        dist_x = self.pos_x - self.old_x
        dist_y = self.pos_y - self.old_y        
        # Update old position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        # Update x position
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
        # Update y position
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
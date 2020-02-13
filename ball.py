import pygame
from random import choice
from math import cos, sin, radians

class Ball:
    """Class to model a bouncing ball"""

    def __init__(self, bb_game):
        """Initialize ball"""
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.radius = self.settings.ball_radius
        self.color = self.settings.ball_color
    
        # initialize old position
        self._init_old_pos()

        # Check ball-bar collisions
        self.bounce = False
        
    def _init_old_pos(self):
        """Function to set rolling direction upon ball instantiation."""
        # Starting position:
        self.pos_x = self.settings.ball_pos_x
        self.pos_y = self.settings.ball_pos_y
        # Old position depending on Theta and speed:
        angles_1 = list(range(self.settings.ball_start_angle, 89))
        angles_2 = list(range(91, self.settings.ball_end_angle))
        theta = choice(angles_1 + angles_2)
        self.old_x = self.settings.ball_speed * cos(radians(theta)) + self.pos_x
        self.old_y = self.settings.ball_speed * sin(radians(theta)) + self.pos_y
        print(self.old_x, self.old_y)

    def update(self):
        """Updates ball position"""
        # Get difference between new and old position
        delta_x = self.pos_x - self.old_x
        delta_y = self.pos_y - self.old_y  
        # Update old position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        # Update x position
        if self.pos_x <= (0 + self.settings.ball_radius) or \
            self.pos_x >= (self.settings.screen_width - self.settings.ball_radius):
            delta_x *= -1
        self.pos_x += delta_x
        # Update y position
        if self.pos_y <= (0 + self.settings.ball_radius) or self.bounce:
            delta_y *= -1
        self.pos_y += delta_y
        self.bounce = False

    def draw_ball(self):
        """Draw the ball on the screen AND store new rect"""
        self.rect = pygame.draw.circle(self.screen, self.color, 
            (int(self.pos_x), int(self.pos_y)), self.radius)
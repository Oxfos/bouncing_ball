import pygame
from pygame.sprite import Sprite

class Bar(Sprite):
    """A class to manage the bar"""

    def __init__(self, bb_game):
        """Initialize the bar and set its starting position."""
        super().__init__()
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        # Load the bar image and get its rect.
        self.rect = pygame.Rect(0,0, self.settings.bar_width, 7)
        
        # Start each new bar at the bottom center of the screen.
        self.center_bar()

        # Initializes movement flag
        self.moving_right = False
        self.moving_left = False

    def center_bar(self):
        """Recenters the bar"""
        # Updating bar width
        self.rect.width = self.settings.bar_width
        # Centering the bar
        self.rect.midbottom = self.screen_rect.midbottom
        # Convert rect.x to float
        self.x = float(self.rect.x)

    def update(self):
        """Update bar position with moving flag"""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.bar_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bar_speed
        # Reconverts self.x to self.rect.x
        self.rect.x = self.x
        # Updating bar width
        self.rect.width = self.settings.bar_width

    def draw_bar(self):
        """Draw the ball at its current location."""
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
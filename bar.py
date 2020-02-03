import pygame

class Bar:
    """A class to manage the bar"""

    def __init__(self, bb_game):
        """Initialize the bar and set its starting position."""
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        # Load the bar image and get its rect.
        self.image = pygame.image.load('images/bar.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new bar at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Initializes movement flag
        self.moving_right = False
        self.moving_left = False
        # Convert rect.x to float
        self.x = float(self.rect.x)

    def update(self):
        """Update bar position with moving flag"""
        if self.moving_right:
            self.x += self.settings.bar_speed
        if self.moving_left:
            self.x -= self.settings.bar_speed
        # REconcerts self.x to self.rect.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
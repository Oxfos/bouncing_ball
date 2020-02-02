import pygame

class Bar:
    """A class to manage the bar"""

    def __init__(self, bb_game):
        """Initialize the bar and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        # Load the bar image and get its rect.
        self.image = pygame.image.load('images/bar.bmp')
        self.rect = self.image.get_rect()

        # Start each new bar at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
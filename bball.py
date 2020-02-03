import sys
import pygame
from bar import Bar

class BouncingBall:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (0,0,255)
        pygame.display.set_caption("Bouncing Ball")
        self.bar = Bar(self)

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Moving right:
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.bar.rect.x += 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.bar.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance + run game.
    bb = BouncingBall()
    bb.run_game()
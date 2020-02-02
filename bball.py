import sys
import pygame

class BouncingBall:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (0,0,255)
        pygame.display.set_caption("Bouncing Ball")

    def run_game(self):
        """Main game loop"""
        while True:
            # Check for keyboard and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw screen
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance + run game.
    bb = BouncingBall()
    bb.run_game()
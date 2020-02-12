import sys
from time import sleep
import pygame
from settings import Settings
from bar import Bar
from ball import Ball
from stats import GameStats
from button import Button

class BouncingBall:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Clock set-up for framerate
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Bouncing Ball")
        self.bar = Bar(self)
        self.ball = Ball(self)
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.bar.update() # implements movement depending on movement flag
                self._ball_checks()
                self.ball.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Pressing arrow keys for movement:
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Releasing arrow keys:
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Checks keydown events."""
        if event.key == pygame.K_RIGHT:
            self.bar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bar.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_play_button(self, mouse_pos):
        """Restart game when Play button is clicked."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.bar.center_bar()
            self._ball_lost()
            self.stats.game_active = True

    def _check_keyup_events(self, event):
        """Checks keyup events."""
        if event.key == pygame.K_RIGHT:
            self.bar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.bar.moving_left = False

    def _ball_checks(self):
        self._check_ball_bar_collision()
        self._check_ball_lost()

    def _check_ball_bar_collision(self):
        if pygame.sprite.collide_rect(self.ball, self.bar):
            print('Bounce!')
            self.ball.bounce = True

    def _check_ball_lost(self):
        """Reset game if ball drops below bottom edge"""
        if self.ball.rect.top >= self.settings.screen_height:
            self._ball_lost()

    def _ball_lost(self):
        """Take action if ball is lost"""
        if self.stats.ball_left > 0:
            self.ball._start()
            self.stats.ball_left -= 1
            sleep(0.5)
        else:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.bar.draw_bar()
        self.ball.draw_ball()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        self.clock.tick(150)


if __name__ == '__main__':
    # Make game instance + run game.
    bb = BouncingBall()
    bb.run_game()
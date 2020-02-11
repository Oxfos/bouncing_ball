import pygame.font

class Button:

    def __init__(self, bb_game, msg):
        """ Initialize button attributes."""
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()
        # Button rect
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Font msg
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Prepares msg to be drawn onto screen.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render msg and place on button. """
        # Creates image from msg.
        self.msg_image = self.font.render(msg, True, self.font_color,
            self.button_color)
        # Gets a rect from image.
        self.msg_image_rect = self.msg_image.get_rect()
        # Centers the image rect with the button rect.
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws button and msg on the screen."""
        # Fills the screen with the rect and color.
        self.screen.fill(self.button_color, self.rect)
        # Draws the image and its rect on the screen.
        self.screen.blit(self.msg_image, self.msg_image_rect)
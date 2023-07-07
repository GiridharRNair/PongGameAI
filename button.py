import pygame

font = pygame.font.Font('freesansbold.ttf', 18)


class Button:
    def __init__(self, text, x_pos, y_pos, enabled, screen):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.screen = screen
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, 'white')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (100, 25))
        if self.check_clicked():
            pygame.draw.rect(self.screen, 'dark grey', button_rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'grey', button_rect, 0, 5)
        pygame.draw.rect(self.screen, 'white', button_rect, 2, 5)
        self.screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_clicked = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        if left_clicked and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

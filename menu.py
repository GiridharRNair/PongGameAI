import pygame
from button import Button

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render('Choose difficulty', True, 'white', 'black')


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([200, 200])
        self.timer = pygame.time.Clock()
        pygame.display.set_caption('Pong AI Difficulty')

        self.buttons = {
            'difficulty_1.pickle': Button('Easy', 10, 15, True, self.screen),
            'difficulty_2.pickle': Button('Medium', 10, 45, True, self.screen),
            'difficulty_3.pickle': Button('Hard', 10, 75, True, self.screen)
        }

    def draw(self):
        run = True
        while run:
            self.screen.fill('black')
            self.timer.tick(60)

            self.screen.blit(text, text.get_rect())

            for button in self.buttons.values():
                button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for name, button in self.buttons.items():
                        if button.check_clicked():
                            return name

            pygame.display.flip()

        pygame.quit()

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_BLUE, MENU_OPTION, C_DARK_BLUE, C_BLACK, C_PURPLE


class Menu:

    def __init__(self, window):

        self.window = window
        self.surf = pygame.image.load('./assets/menu_bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run (self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/menu_music.mp3')
        pygame.mixer_music.play(-1)

        while True:
            #imagens
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(110, 'Frozen', C_BLUE, ((WIN_WIDTH / 2), 100))
            self.menu_text(75, 'Core', C_BLUE, ((WIN_WIDTH / 2), 155))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], C_PURPLE, ((WIN_WIDTH / 2), 520 + 30 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], C_DARK_BLUE, ((WIN_WIDTH / 2), 520 + 30 * i))

            pygame.display.flip()

            #check de event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option =0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="andy bold", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
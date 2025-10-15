import sys
import pygame

from datetime import datetime
from pygame import Surface, Rect, K_RETURN, K_BACKSPACE, KEYDOWN, K_ESCAPE
from pygame.font import Font
from code.Const import C_BLUE, SCORE_POSITION, MENU_OPTION, C_DARK_BLUE, C_LIGHT_BLUE, C_BLACK, C_GREEN, C_YELLOW
from code.DBProxy import DBProxy

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/scorebg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode:str, player_score:list[int]):
        pygame.mixer_music.load('./assets/score_music.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            self.score_text(56,'YOU WON!', C_BLUE, SCORE_POSITION['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player Name: (4 characters)'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team Name: (4 characters)'

            self.score_text(20, text, C_LIGHT_BLUE, SCORE_POSITION['Namein'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) ==4:
                        db_proxy.save({'name':name,'score' : score,'date':get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20,name, C_BLACK, SCORE_POSITION['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./assets/score_music.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'top 10', C_BLACK, SCORE_POSITION['Title'])
        self.score_text(20, 'NAME         SCORE              DATE    ', C_BLACK, SCORE_POSITION['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top()
        db_proxy.close()

        for player_score in list_score:
            id_,name,score,date = player_score
            self.score_text(20,f'{name}     {score :05d}        {date}', C_YELLOW, SCORE_POSITION[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Andy Bold", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_time} - {current_date}'
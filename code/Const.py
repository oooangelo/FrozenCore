import pygame

#C
COLOR_BLUE = (180, 180, 255)
COLOR_DARK_BLUE = (100, 100, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (255, 0, 255)

#E
ENTITY_SPEED = {
    'level1bg0':1,
    'Player1':4,
    'Player2':4,
    'Enemy1': 2,
    'Enemy2': 3,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = ('SOLO - NEW GAME',
               'CO-OP - NEW GAME',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w, }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s, }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d, }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a, }
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL, }

#S
SPAWN_TIME = 500

#W
WIN_WIDTH = 1280
WIN_HEIGHT = 720




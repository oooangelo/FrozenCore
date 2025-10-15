import pygame

#WINDOW
WIN_WIDTH = 1280
WIN_HEIGHT = 720

#C
C_BLUE = (180, 180, 255)
C_DARK_BLUE = (100, 100, 255)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_PURPLE = (255, 0, 255)
C_CYAN = (0, 255, 255)
C_RED = (255, 20, 20)
C_GREEN = (0, 128, 0)
C_YELLOW = (255, 215, 0)
C_PINK = (255, 0, 255)
C_LIGHT_BLUE = (189, 255, 255)

#E
ENTITY_SPEED = {
    'level1bg0':1,
    'level2bg0':1,
    'level3bg0':1,
    'Player1':4,
    'Player2':4,
    'Enemy1': 2,
    'Enemy2': 3,
    'Player1Shoot': 6,
    'Player2Shoot': 6,
    'Enemy1Shoot' :3,
    'Enemy2Shoot' :4,
}

ENTITY_HEALTH = {
    'level1bg0':42000,
    'level2bg0':42000,
    'level3bg0':42000,
    'Player1':300,
    'Player2':300,
    'Enemy1': 50,
    'Enemy2': 25,
    'Player1Shoot': 1,
    'Player2Shoot': 1,
    'Enemy1Shoot': 1,
    'Enemy2Shoot': 1,
}


EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SHOOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1' : 200,
    'Enemy2': 200,
}

ENTITY_DAMAGE = {
    'level1bg0':0,
    'level2bg0':0,
    'level3bg0':0,
    'Player1':50,
    'Player2':50,
    'Enemy1': 10,
    'Enemy2': 10,
    'Player1Shoot': 25,
    'Player2Shoot': 30,
    'Enemy1Shoot': 15,
    'Enemy2Shoot': 10,
}

ENTITY_SCORE = {
    'level1bg0':0,
    'level2bg0':0,
    'level3bg0':0,
    'Player1':0,
    'Player2':0,
    'Enemy1': 100,
    'Enemy2': 150,
    'Player1Shoot': 0,
    'Player2Shoot': 0,
    'Enemy1Shoot': 0,
    'Enemy2Shoot': 0,
}

#M
MENU_OPTION = ('SOLO - NEW GAME',
               'CO-OP - NEW GAME',
               'SCORE',
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
SPAWN_TIME = 400

SCORE_POSITION = {'Title' : (WIN_WIDTH/2, 50),
                  'Namein' : (WIN_WIDTH/2, 90),
                  'Label' : (WIN_WIDTH/2, 100),
                  "Name" : (WIN_WIDTH/2, 120),
                  0 : (WIN_WIDTH/2, 120),
                  1 : (WIN_WIDTH/2, 150),
                  2 : (WIN_WIDTH/2, 180),
                  3 : (WIN_WIDTH/2, 210),
                  4 : (WIN_WIDTH/2, 240),
                  5 : (WIN_WIDTH/2, 270),
                  6 : (WIN_WIDTH/2, 300),
                  7 : (WIN_WIDTH/2, 330),
                  8 : (WIN_WIDTH/2, 360),
                  9 : (WIN_WIDTH/2, 390)
}

#T

TIMEOUT_C = 100 # 1 segundo

TIMEOUT_LEVEL = 30000 #30 segundos de fase = 30000




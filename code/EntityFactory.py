import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'level1bg{i}', (0,0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (20,WIN_HEIGHT/2 - 30))
            case 'Player2':
                return Player('Player2', (20,WIN_HEIGHT/2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(20, WIN_HEIGHT - 20)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(20, WIN_HEIGHT - 20)))

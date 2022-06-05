import pygame
from settings import Settings
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name , pos ,groups) -> None:
        super().__init__(groups)
        
        self.sprite_type = "enemy"
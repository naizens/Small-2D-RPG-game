import pygame, os
from settings import Settings

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load(os.path.join(Settings.test_path,"player.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
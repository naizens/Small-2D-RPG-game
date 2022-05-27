import pygame, os
from settings import Settings

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((Settings.tilesize, Settings.tilesize))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        #self.image = pygame.image.load(os.path.join(Settings.test_path,"fence.png")).convert_alpha()
        self.x, self.y = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.x*Settings.scaling, self.y*Settings.scaling))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -20)
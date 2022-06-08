import pygame, os
from settings import Settings

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((Settings.tilesize, Settings.tilesize))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        
        self.x, self.y = self.image.get_size()
        
        self.image = pygame.transform.scale(self.image, (self.x*Settings.scaling, self.y*Settings.scaling))

        self.rect = self.image.get_rect(bottomleft = (pos[0], pos[1] + Settings.tilesize*Settings.scaling))
        
        self.hitbox = self.rect.inflate(0, -20)
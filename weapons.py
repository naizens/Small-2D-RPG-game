import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups) -> None:
        super().__init__(groups)
        directon = player.staus
        
        #graphics
        self.image = pygame.Surface((40, 40))
        
        #placement
        self.rect = self.image.get_rect(center = player.rect.center)
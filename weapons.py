from re import S
import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups) -> None:
        super().__init__(groups)
        directon = player.status.split("_", 1)[0]
        print(directon)
        
        #graphics
        self.image = pygame.Surface((40, 40))
        
        #placement
        if directon == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-4, 16))
        elif directon == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(4, 16))
        elif directon == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-16, 4))
        elif directon == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-16, 0))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
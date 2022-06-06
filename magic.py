import pygame, os
from settings import Settings
from random import randint

class MagicPlayer():
    def __init__(self, animation_player) -> None:
        self.animation_player = animation_player
        
        self.heal_sound = pygame.mixer.Sound(os.path.join(Settings.sound_path, "heal.wav"))
        self.heal_sound.set_volume(Settings.volume)
        self.flame_sound = pygame.mixer.Sound(os.path.join(Settings.sound_path, "fire.wav"))
        self.flame_sound.set_volume(Settings.volume)
        
    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:

            self.heal_sound.play()
            player.energy -= cost
            player.health += strength
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]
            self.animation_player.create_particles("aura", player.rect.center, groups)
            self.animation_player.create_particles("heal", player.rect.center + pygame.math.Vector2(0,-60), groups)
            
        
    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            self.flame_sound.play()
            if player.status.split("_")[0] == "right":
                direction = pygame.math.Vector2(1,0)
        
            elif player.status.split("_")[0] == "left":
                direction = pygame.math.Vector2(-1,0)
                
            elif player.status.split("_")[0] == "up":
                direction = pygame.math.Vector2(0,-1)
                
            else:
                direction = pygame.math.Vector2(0,1)
                
            for i in range(1, 5):
                if direction.x:
                    offset_x = (direction.x * i) * Settings.tilesize * Settings.scaling
                    x = player.rect.centerx + offset_x + randint(-(Settings.tilesize * Settings.scaling) // 3, (Settings.tilesize * Settings.scaling))
                    y = player.rect.centery + randint(-(Settings.tilesize * Settings.scaling) // 3, (Settings.tilesize * Settings.scaling))
                    self.animation_player.create_particles("flame", (x,y), groups)
                else:
                   offset_y = (direction.y * i) * Settings.tilesize * Settings.scaling
                   x = player.rect.centerx + randint(-(Settings.tilesize * Settings.scaling) // 3, (Settings.tilesize * Settings.scaling))
                   y = player.rect.centery + offset_y + randint(-(Settings.tilesize * Settings.scaling) // 3, (Settings.tilesize * Settings.scaling))
                   self.animation_player.create_particles("flame", (x,y), groups)
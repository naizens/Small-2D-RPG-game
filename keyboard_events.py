import pygame
from settings import Settings

class Inputs():
    def __init__(self, game) -> None:

        self.game = game

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                    self.game.running = False

            ## Movement Keys
            if not self.game.level.player.attacking:
                if keys[pygame.K_w]:
                    self.game.level.player.direction.y = -1
                    self.game.level.player.status = "up"
                elif keys[pygame.K_s]:
                    self.game.level.player.direction.y = 1
                    self.game.level.player.status = "down"
                else:
                    self.game.level.player.direction.y = 0

                if keys[pygame.K_d]:
                    self.game.level.player.direction.x = 1
                    self.game.level.player.status = "right"
                elif keys[pygame.K_a]:
                    self.game.level.player.direction.x = -1
                    self.game.level.player.status = "left"
                else:
                    self.game.level.player.direction.x = 0
                
            ## Attack Keys
                if keys[pygame.K_SPACE]:
                    self.game.level.player.attacking = True
                    self.attack_time = pygame.time.get_ticks()
                    self.game.level.player.create_attack()
                    print("Attack")
                    
                ## Magic Key
                
                if keys[pygame.K_LCTRL]:
                    self.game.level.player.attacking = True
                    self.attack_time = pygame.time.get_ticks()
                    print("Magic")
                
                    
                if keys[pygame.K_q] and self.game.level.player.can_switch_weapon:
                    
                    self.game.level.player.can_switch_weapon = False
                    self.game.level.player.weapon_switch_time = pygame.time.get_ticks()
                    
                    if self.game.level.player.weapon_index > 0:
                        self.game.level.player.weapon_index -= 1
                    else:
                        self.game.level.player.weapon_index = 4

                    self.game.level.player.weapon = list(Settings.weapon_data.keys())[self.game.level.player.weapon_index]
                 
                   
                if keys[pygame.K_e] and self.game.level.player.can_switch_weapon:
                    
                    self.game.level.player.can_switch_weapon = False
                    self.game.level.player.weapon_switch_time = pygame.time.get_ticks()
                    
                    if self.game.level.player.weapon_index < len(list(Settings.weapon_data)) - 1:
                        self.game.level.player.weapon_index += 1
                    else:
                        self.game.level.player.weapon_index = 0

                    self.game.level.player.weapon = list(Settings.weapon_data.keys())[self.game.level.player.weapon_index]

"""     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            # Checks for events if a key is pressed

                if event.key == pygame.K_UP:
                    self.game.level.player.direction.y = -1
                elif event.key == pygame.K_DOWN:
                    self.game.level.player.direction.y = 1
                elif event.key == pygame.K_LEFT:
                    self.game.level.player.direction.x = -1
                elif event.key == pygame.K_RIGHT:
                    self.game.level.player.direction.x = 1
                
                
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    self.game.level.player.direction.y = 0
                elif event.key == pygame.K_DOWN:
                    self.game.level.player.direction.y = 0
                elif event.key == pygame.K_LEFT:
                    self.game.level.player.direction.x = 0
                elif event.key == pygame.K_RIGHT:
                    self.game.level.player.direction.x = 0
"""
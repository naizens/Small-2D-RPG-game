import pygame
from settings import Settings

class Inputs():
    def __init__(self, game) -> None:

        self.game = game

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game.start_screen.start_is_hovered():
                            self.game.game_starting = False
                    elif self.game.start_screen.exit_is_hovered():
                        self.game.running = False
                        
                    if self.game.pause_screen.resume_is_hovered():
                        self.game.game_paused = False
                    elif self.game.pause_screen.exit_is_hovered():
                        self.game.running = False
                        
                    if self.game.gameover_screen.restart_is_hovered():
                        pass
                        #self.game.game.restart()
                    elif self.game.gameover_screen.exit_is_hovered():
                        self.game.running = False
                        
                    
                    
                            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
                self.game.game_paused = True

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
                self.game.level.player.weapon_attack_sound.play()
                
            ## Magic Key
            
            if keys[pygame.K_LCTRL]:
                self.game.level.player.attacking = True
                self.attack_time = pygame.time.get_ticks()
                
                style = list(Settings.magic_data.keys())[self.game.level.player.magic_index]
                strength = list(Settings.magic_data.values())[self.game.level.player.magic_index]["strength"] + self.game.level.player.stats["magic"]
                cost = list(Settings.magic_data.values())[self.game.level.player.magic_index]["cost"]
                self.game.level.player.create_magic(style, strength, cost)
                
            if keys[pygame.K_q] and self.game.level.player.can_switch_weapon:
                
                self.game.level.player.can_switch_weapon = False
                self.game.level.player.weapon_switch_time = pygame.time.get_ticks()
                
                if self.game.level.player.weapon_index < len(list(Settings.weapon_data)) - 1:
                    self.game.level.player.weapon_index += 1
                else:
                    self.game.level.player.weapon_index = 0

                self.game.level.player.weapon = list(Settings.weapon_data.keys())[self.game.level.player.weapon_index]
                
                
            if keys[pygame.K_e] and self.game.level.player.can_switch_magic:
                
                self.game.level.player.can_switch_magic = False
                self.game.level.player.magic_switch_time = pygame.time.get_ticks()
                
                if self.game.level.player.magic_index < len(list(Settings.magic_data)) - 1:
                    self.game.level.player.magic_index += 1
                else:
                    self.game.level.player.magic_index = 0

                self.game.level.player.magic = list(Settings.magic_data.keys())[self.game.level.player.magic_index]
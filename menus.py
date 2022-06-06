import pygame, os
from settings import Settings


class StartScreen():
    def __init__(self):
        
        pygame.font.init()
        
        self.font = pygame.font.Font(Settings.ui_font, 60)
        
        button_path = os.path.join(Settings.image_path, "buttons")
        
        self.image = pygame.image.load(os.path.join(Settings.image_path,"start_bg.jpg")).convert_alpha()
        self.image = pygame.transform.scale(self.image,(Settings.width, Settings.heigth))
        
        self.start_button = pygame.image.load(os.path.join(button_path,"start_button.png")).convert_alpha()
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.topleft = (Settings.width//2 - self.start_button_rect.width//2, Settings.heigth//2 - self.start_button_rect.height // 2 - 5)
        
        self.exit_button = pygame.image.load(os.path.join(button_path,"exit_button.png")).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.topleft = (Settings.width//2 - self.exit_button_rect.width//2, Settings.heigth//2 + self.exit_button_rect.height // 2 + 5)
        
        self.info_text = self.font.render(("Welcome to the game!"), 1 , "red")
        
    def start_is_hovered(self):
        return self.start_button_rect.collidepoint(pygame.mouse.get_pos())    
    
    def exit_is_hovered(self):
        return self.exit_button_rect.collidepoint(pygame.mouse.get_pos())
    
    def draw(self, screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.info_text, (Settings.width // 2 - self.info_text.get_rect().width // 2, Settings.heigth // 2 - self.info_text.get_rect().height // 2 - self.start_button_rect.height - 100))
        screen.blit(self.start_button, self.start_button_rect)
        screen.blit(self.exit_button, self.exit_button_rect)
        
class PauseScreen():
    def __init__(self):
        pass
        
    def draw(self, screen):
        
        screen.blit(self.image,(0,0))
        
class GameOverScreen():
    def __init__(self):
        pass
        
        
    def draw(self, screen):
        
        screen.blit(self.image,(0,0))
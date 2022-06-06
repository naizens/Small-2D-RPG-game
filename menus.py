import pygame, os
from settings import Settings

button_path = os.path.join(Settings.image_path, "buttons")

class StartScreen():
    def __init__(self):
        
        pygame.font.init()
        
        self.font = pygame.font.Font(Settings.ui_font, 60)
        
        
        self.image = pygame.image.load(os.path.join(Settings.image_path,"start_bg.jpg")).convert_alpha()
        self.image = pygame.transform.scale(self.image,(Settings.width, Settings.heigth))
        
        self.start_button = pygame.image.load(os.path.join(button_path,"start_button.png")).convert_alpha()
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.topleft = (Settings.width//2 - self.start_button_rect.width//2, Settings.heigth//2 - self.start_button_rect.height // 2 - 20)
        
        self.exit_button = pygame.image.load(os.path.join(button_path,"exit_button.png")).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.topleft = (Settings.width//2 - self.exit_button_rect.width//2, Settings.heigth//2 + self.exit_button_rect.height // 2 + 20)
        
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
        
        self.overlay = pygame.Surface((Settings.width, Settings.heigth))
        self.overlay.set_alpha(30)
        pygame.Surface.fill(self.overlay, (136, 136, 136))
        
        self.pause_banner = pygame.image.load(os.path.join(button_path,"pause_banner.png")).convert_alpha()
        self.pause_banner_rect = self.pause_banner.get_rect()
        self.pause_banner_rect.topleft = (Settings.width // 2 - self.pause_banner_rect.width // 2, Settings.heigth // 2 - self.pause_banner_rect.height // 2.5)
        
        self.back_button = pygame.image.load(os.path.join(button_path,"back_button.png")).convert_alpha()
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.topleft = (Settings.width // 2 - self.back_button_rect.width // 2, Settings.heigth // 2 - self.back_button_rect.height // 2 - 10)
        
        self.exit_button = pygame.image.load(os.path.join(button_path,"exit_button.png")).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.topleft = (Settings.width // 2 - self.exit_button_rect.width // 2, Settings.heigth // 2 + self.exit_button_rect.height // 2 + 10)
        
    def resume_is_hovered(self):
        return self.back_button_rect.collidepoint(pygame.mouse.get_pos())    
    
    def exit_is_hovered(self):
        return self.exit_button_rect.collidepoint(pygame.mouse.get_pos())
        
    def draw(self, screen):
        screen.blit(self.overlay, self.overlay.get_rect())
        screen.blit(self.pause_banner, self.pause_banner_rect)
        screen.blit(self.back_button, self.back_button_rect)
        screen.blit(self.exit_button, self.exit_button_rect)
        
        
        
class GameOverScreen():
    def __init__(self):
        pass
        
        
    def draw(self, screen):
        
        screen.blit(self.image,(0,0))
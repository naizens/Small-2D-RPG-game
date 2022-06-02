import pygame
from settings import Settings

class Ui:
    def __init__(self) -> None:
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(Settings.ui_font, Settings.ui_font_size)
        
        # bar setup
        self.healt_bar_rect = pygame.Rect(10, 10, Settings.health_bar_width, Settings.bar_height)
        self.energy_bar_rect = pygame.Rect(10, 34 , Settings.energy_bar_width, Settings.bar_height)
    
    def show_bar(self, current, max_ammount, bg_rect, color):
        pygame.draw.rect(self.display_surface, Settings.ui_bg_color, bg_rect)
        
        ratio = current / max_ammount
        current_width = ratio * bg_rect.width
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        
        pygame.draw.rect(self.display_surface, color, current_rect)
    
    def display(self, player):
        self.show_bar(player.health, player.stats["health"], self.healt_bar_rect, Settings.health_color)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, Settings.energy_color)
        
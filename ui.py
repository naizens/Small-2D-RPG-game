import pygame
from settings import Settings

class Ui:
    def __init__(self) -> None:
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(Settings.font_path, Settings.font_size)
    
    def display(self, player):
        pass
import pygame
from settings import Settings
from weapons import Weapon

class Ui:
    def __init__(self) -> None:
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(Settings.ui_font, Settings.ui_font_size)
        
        # bar setup
        self.healt_bar_rect = pygame.Rect(10, 10, Settings.health_bar_width, Settings.bar_height)
        self.energy_bar_rect = pygame.Rect(10, 34 , Settings.energy_bar_width, Settings.bar_height)
        
        #convert weapon dict to list
        self.weapon_graphics = []
        for weapon in Settings.weapon_data.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)
    
    def show_bar(self, current, max_ammount, bg_rect, color):
        pygame.draw.rect(self.display_surface, Settings.ui_bg_color, bg_rect, border_radius = Settings.ui_border_radius)
        
        ratio = current / max_ammount
        current_width = ratio * bg_rect.width
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        pygame.draw.rect(self.display_surface, color, current_rect, border_radius = Settings.ui_border_radius)
        pygame.draw.rect(self.display_surface, Settings.ui_border_color, bg_rect, 3, border_radius = Settings.ui_border_radius)
    
    def show_exp(self, exp):
        text_surface = self.font.render(str(int(exp)), False, Settings.ui_text_color)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surface.get_rect(bottomright = (x, y))
        
        pygame.draw.rect(self.display_surface, Settings.ui_bg_color, text_rect.inflate(10, 10), border_radius = Settings.ui_border_radius)
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, Settings.ui_border_color, text_rect.inflate(10, 10), 3 , border_radius = Settings.ui_border_radius)
    
    def item_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, Settings.item_box_size, Settings.item_box_size)
        pygame.draw.rect(self.display_surface, Settings.ui_bg_color, bg_rect, border_radius = Settings.ui_border_radius)
        if has_switched:
            pygame.draw.rect(self.display_surface, Settings.ui_border_color_active, bg_rect, 3 ,border_radius = Settings.ui_border_radius)
        else:
            pygame.draw.rect(self.display_surface, Settings.ui_border_color, bg_rect, 3 ,border_radius = Settings.ui_border_radius)
        return bg_rect
    
    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.item_box(Settings.width // 2 - Settings.item_box_size // 2 , Settings.heigth - (Settings.item_box_size + 10), has_switched)
        weapon_surface = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surface.get_rect(center = bg_rect.center)
        
        self.display_surface.blit(weapon_surface, weapon_rect)
        
    def draw(self, player):
        self.show_bar(player.health, player.stats["health"], self.healt_bar_rect, Settings.health_color)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, Settings.energy_color)
        
        self.show_exp(player.exp)
        
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        
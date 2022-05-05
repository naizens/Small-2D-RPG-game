import pygame
from settings import Settings
from tile import Tile
from player import Player

class Level():
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()  # Group of sprites that are visible
        self.obstacle_sprites = pygame.sprite.Group() # Group of the sprites that the Player can collide with


        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(Settings.world_map):
            for col_index, col in enumerate(row):
                x = col_index * Settings.tilesize
                y = row_index * Settings.tilesize
                if col == "x":
                    Tile((x,y),[self.visible_sprites])



    def update(self):
        pass
    def draw(self):

        self.visible_sprites.draw(self.display_surface)

    
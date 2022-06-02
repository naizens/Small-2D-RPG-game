import pygame
import os
import random

from settings import Settings
from tile import Tile
from player import Player
from support import import_csv_layout, import_folder
from weapons import Weapon
from ui import Ui

class Level():
    def __init__(self, game):
        
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Create sprite groups
        self.visible_sprites = YSortCameraGroup()  # Group of sprites that are visible
        self.obstacle_sprites = pygame.sprite.Group() # Group of the sprites that the Player can collide with

        self.game = game
        
        # Sprites for the attack
        self.current_attack = None
        
        # Setup for the Sprites
        self.create_map()
        
        # Ui
        self.ui = Ui()

    def create_map(self):
        layouts = {
            "boundary": import_csv_layout(os.path.join(Settings.map_path,"map_FloorBlocks.csv")),
            "objects": import_csv_layout(os.path.join(Settings.map_path,"map_objects.csv")),
            "animals": import_csv_layout(os.path.join(Settings.map_path,"map_animals.csv")),
            "entitys": import_csv_layout(os.path.join(Settings.map_path,"map_Entitys.csv")),          
            }
        graphics = {
            "animals": import_folder(Settings.animal_path),
            "objects": import_folder(Settings.object_path),
            "entitys": import_folder(Settings.monster_path),
        }
        
        
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * Settings.tilesize * Settings.scaling
                        y = row_index * Settings.tilesize * Settings.scaling
                        if style == "boundary":
                            Tile((x,y),[self.obstacle_sprites], "invisible")
                            
                        if style == "objects":
                            surf = graphics["objects"][col]
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites], "object", surf)
                            
                        if style == "animals":
                            random_animal = graphics["animals"][random.choice(list(graphics["animals"]))]
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites], "animal", random_animal)
                        
                        if style == "entitys":
                            if col == "0":
                                self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites, self.game, self.create_attack, self.destroy_attack)
                            else:
                                random_entity = graphics["entitys"][random.choice(list(graphics["entitys"]))]
                                Tile((x,y),[self.visible_sprites, self.obstacle_sprites], "entity", random_entity)
                            
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
        
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def update(self):
        self.visible_sprites.update()
        
        
    def draw(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_heigth = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(10,20)

        self.floor_surface = pygame.image.load(os.path.join(Settings.image_path,"floor.png")).convert_alpha()
        self.x, self.y = self.floor_surface.get_size()
        self.floor_surface = pygame.transform.scale(self.floor_surface, (self.x*Settings.scaling, self.y*Settings.scaling))
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
        
    def custom_draw(self, player):

        #get the offset
        self.offset.x = player.rect.x - self.half_width
        self.offset.y = player.rect.y - self.half_heigth
        
        #draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
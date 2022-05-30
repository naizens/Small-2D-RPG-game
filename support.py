from csv import reader
import os 
from settings import Settings
import pygame

animal_path = os.path.join(Settings.image_path, "animals")
monster_path = os.path.join(Settings.image_path, "monsters")

def import_csv_layout(path):
    terrain_map = []
    with open (path, "r") as level_map:
        layout = reader(level_map, delimiter= ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = {}
    
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_test = image.replace(".png","")
            surface_list[image_test] = image_surf
            # surface_list.append(image_surf)
            
    return surface_list   


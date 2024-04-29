import pygame, os
from settings import Settings
from entity import Entity
from support import import_folder


class Animal(Entity):
    def __init__(self, animal_name , pos ,groups, obstacle_sprites) -> None:
        super().__init__(groups)
        self.sprite_type = "animal"
        
        self.import_graphics(animal_name)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]
        self.animation_speed = 0.05
       
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50, -40)
        self.obstacle_sprites = obstacle_sprites
        
        
        self.animal_name = animal_name
        animal_info = Settings.animal_data[self.animal_name]
        
        self.health = animal_info["health"]
        self.notice_radius = animal_info["notice_radius"]
        
    def import_graphics(self, name):
        self.animations = {"idle": []}
        main_path = os.path.join(Settings.animal_path, name)
        
        for animation in self.animations.keys():
            full_path = os.path.join(main_path, animation)
            self.animations[animation] = list(import_folder(full_path).values())
            
    def animate(self):
        animation = self.animations[self.status]
        
        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
           
    def update(self):
        self.animate()
        
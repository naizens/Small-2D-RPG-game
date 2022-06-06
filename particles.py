import pygame, os
from support import import_folder
from settings import Settings

class AnimationPlayer():
    def __init__(self) -> None:
        
        particle_path = os.path.join(Settings.image_path, "particles")
        flame_path = os.path.join(particle_path, "flame")
        aura_path = os.path.join(particle_path, "aura")
        heal_path = os.path.join(particle_path, "heal")
        smoke_path = os.path.join(particle_path, "smoke")
        
        flames = os.path.join(flame_path, "frames")
        
        self.frames = {
            
			# magic
			"flame": import_folder(flames),
			"aura": import_folder(aura_path),
			"heal": import_folder(os.path.join(heal_path, "frames")),
			
			# attacks 
			"claw": import_folder(os.path.join(particle_path, "claw")),
			"slash": import_folder(os.path.join(particle_path, "slash")),

			# monster deaths
			"wolf": import_folder(smoke_path),
			"slime": import_folder(smoke_path),
			"skeleton": import_folder(smoke_path)
			
        }

        
    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)
        
        
class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos , animation_frames, groups) -> None:
        super().__init__(groups)
        self.sprite_type = 'magic'
        
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[str(self.frame_index)]
        self.rect = self.image.get_rect(center = pos)
        

        
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[str(int(self.frame_index))]
            
    def update(self):
        self.animate()
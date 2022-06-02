import pygame, os
from settings import Settings
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, game, create_attack, destroy_attack, create_magic):
        super().__init__(groups)
        
        self.game = game
        
        self.image = pygame.image.load(os.path.join(Settings.idle_player_path,"idle_down.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50, -60)

        # Setup for the graphics
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.15
        
        # Parameters for movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites
        
        #Weapon setup
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 3
        self.weapon = list(Settings.weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cd = 200
        
        # Magic spell setup
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(Settings.magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None
        
        # Stats of the Player
        self.stats = Settings.player_stats
        self.health = self.stats["health"] * 0.8
        self.energy = self.stats["energy"]
        self.exp = 187
        self.speed = self.stats["speed"]
               

    def import_player_assets(self):
        character_path = Settings.character_path
        self.animations = {"up": [], "down": [], "left": [], "right": [], "right_idle": [],
                          "left_idle": [], "up_idle": [], "down_idle": [],"right_attack": [],
                          "left_attack": [], "up_attack": [], "down_attack": []}
        
        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = list(import_folder(full_path).values())

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status and not "attack" in self.status:
                self.status = self.status + "_idle"
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status and not "idle" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_attack")
                else:
                    self.status = self.status + "_attack"
        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")
        
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        #self.rect.center += self.direction * speed
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.game.input_manager.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()
                
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cd:
                self.can_switch_weapon = True
                
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cd:
                self.can_switch_magic = True
    
    def animate(self):
        animation = self.animations[self.status]
        
        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    def update(self):
        self.cooldowns()
        self.get_status()
        self.move(self.speed)
        
    def draw(self):
        self.animate()
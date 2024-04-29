import os

class Settings():
    width = 1280
    heigth = 720
    fps = 60

    title = "2D-RPG-Game"
    volume = 0.2

    # General Path setup
    file_path = os.path.dirname(os.path.abspath(__file__))
    asset_path = os.path.join(file_path, "assets")
    image_path = os.path.join(asset_path, "images")
    sound_path = os.path.join(asset_path, "sounds")
    font_path = os.path.join(asset_path, "fonts")
    test_path = os.path.join(asset_path, "test")
    
    # Specific Path setup
    
    attack_sound_path = os.path.join(sound_path, "attack")
    
    ## Pathes for the images
    object_path = os.path.join(image_path, "objects")
    animal_path = os.path.join(image_path, "animals")
    monster_path = os.path.join(image_path, "monsters")
    character_path = os.path.join(image_path, "player")
    weapon_path = os.path.join(image_path, "weapons")
    player_path = os.path.join(image_path, "player")
    particle_path = os.path.join(image_path, "particles")
    idle_player_path = os.path.join(character_path, "down_idle")
    
    ## Pathes for the weapons
    sword_path = os.path.join(weapon_path, "sword")
    lance_path = os.path.join(weapon_path, "lance")
    axe_path = os.path.join(weapon_path, "axe")
    rapier_path = os.path.join(weapon_path, "rapier")
    sai_path = os.path.join(weapon_path, "sai")
    
    ## Paths for the magic spells
    
    fire_path = os.path.join(particle_path, "flame")
    heal_path = os.path.join(particle_path, "heal")

    ## Path for the "maps"/csv-files
    map_path = os.path.join(asset_path, "map")

    # For the Size of the Tiles and the scaling of the Tiles
    tilesize = 16 # set the tilesize to 16x16
    scaling = 4 # parameter to scale the images
    
    # Ui
    bar_height = 20
    health_bar_width = 200
    energy_bar_width = 140
    item_box_size = 80
    ui_font = os.path.join(font_path, "CompassPro.ttf")
    ui_font_size = 25
    ui_border_radius = 10
    
    # General colors
    water_color = "#4fa4b8"
    ui_bg_color = "#302f2f"
    ui_border_color = "#111111"
    ui_text_color = "#eeeeee"
    ui_border_color_active = "#ffd700"
    
    # Ui colors
    health_color = "#e34230"
    energy_color = "#5373e6"
    
    
    weapon_data = {
        "sword": {"cooldown": 100, "damage": 15,"graphic": os.path.join(sword_path, "sword.png")},
        "lance": {"cooldown": 400, "damage": 30,"graphic": os.path.join(lance_path, "lance.png")},
        "axe": {"cooldown": 300, "damage": 20,"graphic": os.path.join(axe_path, "axe.png")},
        "rapier": {"cooldown": 50, "damage": 8,"graphic": os.path.join(rapier_path, "rapier.png")},
        "sai": {"cooldown": 80, "damage": 10,"graphic": os.path.join(sai_path, "sai.png")}
    }
    
    magic_data = {
        "flame": {"strength": 5, "cost": 20, "graphic": os.path.join(fire_path, "fire.png")},
        "heal": {"strength": 20, "cost": 10, "graphic": os.path.join(heal_path, "heal.png")},
    }
    
    player_stats = {"health": 100, "energy": 100, "attack": 10, "magic": 4, "speed": 5}
    
    # Enemys:
    
    monster_data = {
        "slime": {"health": 80, "exp": 100, "damage": 8, "attack_type": "slash", 
                  "attack_sound": os.path.join(attack_sound_path, "slime_attack.wav"), 
                  "speed": 1.5, "resistance": 3 , "attack_radius": 40, "notice_radius": 280},
        
        "wolf": {"health": 60, "exp": 120, "damage": 20, "attack_type": "claw", 
                  "attack_sound": os.path.join(attack_sound_path, "wolf_attack.wav"), 
                  "speed": 3, "resistance": 3 , "attack_radius": 60, "notice_radius": 340},
        
        "skeleton": {"health": 90, "exp": 110, "damage": 12, "attack_type": "slash", 
                  "attack_sound": os.path.join(attack_sound_path, "skeleton_attack.wav"), 
                  "speed": 2, "resistance": 3 , "attack_radius": 50, "notice_radius": 300},
        
        "ogre": {"health": 200, "exp": 220, "damage": 45, "attack_type": "slash", 
                  "attack_sound": os.path.join(attack_sound_path, "ogre_attack.wav"), 
                  "speed": 2, "resistance": 4 , "attack_radius": 70, "notice_radius": 320}
    }
    
    animal_data = {
        "hen": {"health": 80, "notice_radius": 280},
        
        "pig": {"health": 60, "notice_radius": 340}
    }
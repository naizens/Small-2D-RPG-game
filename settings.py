import os

class Settings():
    width = 1280
    heigth = 720
    fps = 60

    title = "2D-RPG-Game"
    volume = 0.1

    # General Path setup
    file_path = os.path.dirname(os.path.abspath(__file__))
    asset_path = os.path.join(file_path, "assets")
    image_path = os.path.join(asset_path, "images")
    sound_path = os.path.join(asset_path, "sounds")
    font_path = os.path.join(asset_path, "fonts")
    test_path = os.path.join(asset_path, "test")
    
    # Pathes for the images
    object_path = os.path.join(image_path, "objects")
    animal_path = os.path.join(image_path, "animals")
    monster_path = os.path.join(image_path, "monsters")
    character_path = os.path.join(image_path, "player")
    weapon_path = os.path.join(image_path, "weapons")
    player_path = os.path.join(image_path, "player")
    idle_player_path = os.path.join(character_path, "down_idle")
    
    #pathes for the weapons
    sword_path = os.path.join(weapon_path, "sword")
    lance_path = os.path.join(weapon_path, "lance")
    axe_path = os.path.join(weapon_path, "axe")
    rapier_path = os.path.join(weapon_path, "rapier")
    sai_path = os.path.join(weapon_path, "sai")

    # Path for the "maps"/csv-files
    map_path = os.path.join(asset_path, "map")

    # For the Size of the Tiles and the scaling of the Tiles
    tilesize = 16 # set the tilesize to 16x16
    scaling = 4 # parameter to scale the images
    
    # Ui
    bar_height = 20
    health_bar_width = 200
    energy_bar_width = 140
    item_box_size = 80
    
    weapon_data = {
        "sword": {"cooldown": 100, "damage": 15,"graphic": os.path.join(sword_path, "sword.png")},
        "lance": {"cooldown": 400, "damage": 30,"graphic": os.path.join(lance_path, "lance.png")},
        "axe": {"cooldown": 300, "damage": 20,"graphic": os.path.join(axe_path, "axe.png")},
        "rapier": {"cooldown": 50, "damage": 8,"graphic": os.path.join(rapier_path, "rapier.png")},
        "sai": {"cooldown": 80, "damage": 10,"graphic": os.path.join(sai_path, "sai.png")}
    }
    
    player_stats = {"health": 100, "energy": 100, "attack": 10, "magic": 4, "speed": 5}
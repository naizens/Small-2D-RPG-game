import os

class Settings():
    width = 1280
    heigth = 720
    fps = 60

    title = "2D-RPG-Game"
    volume = 0.1

    file_path = os.path.dirname(os.path.abspath(__file__))
    asset_path = os.path.join(file_path, "assets")
    
    image_path = os.path.join(asset_path, "images")
    animal_path = os.path.join(image_path, "animals")
    monster_path = os.path.join(image_path, "monsters")
    
    map_path = os.path.join(asset_path, "map")
    sound_path = os.path.join(asset_path, "sounds")
    
    test_path = os.path.join(asset_path, "test")
    
    

    tilesize = 16 # put on 64 for testing purposes change to 16 for production
    scaling = 2 # parameter to scale the images
    
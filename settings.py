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
    sound_path = os.path.join(asset_path, "sounds")

    tilesize = 16 # 16x16 tiles
    

    
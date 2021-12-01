import os.path
import json

class Settings:

    def __init__(self):

        if os.path.exists('config.ini'):
            #TODO реализовать загрузку из файла
            pass
        else:
            #TODO set default setting
            self.screen_width = 1000
            self.screen_height = 410
            self.players_count = 4
        self.maps = []

        with open("source\map\manifest.json", "r") as read_file:
            maps = json.load(read_file)

        for map in maps:
            self.maps.append((map, map + ".txt"))

        self.img_background = "source\img\map.bmp"
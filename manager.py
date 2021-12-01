import random
import sys

from character import Character
from map import Map

class Manager:

    def __init__(self):
        self.characters = {}
        self.map = None
        pass

    def create_map(self):

        map = Map()
       # for y in range(40):
            #for x in range(40):
                #print(x,y)
                #field = Field(x,y)
        pass

    def create_character(self, setting):

        for i in range(1, setting.players_count):
            #self.characters[i] = "plaer_" + str(i)
            self.characters[i] = Character(1,2,1,1,1)

        print(self.characters)
        pass

    def make_move(self):
        # TODO Внешний цикл по героям
        repeat_count = 0

        while True:
            cube_1 = random.randint(1, 6)
            cube_2 = random.randint(1, 6)
            repeat_count = repeat_count + 1
            print(cube_1, cube_2, repeat_count)

            if repeat_count == 3:
                #TODO Отправить в тюрьму
                break

            #TODO переместить фишку
            if (cube_1 != cube_2):
                break

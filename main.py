import pygame
import pygame_menu
import sys

from setting import Settings
from manager import Manager

setting = Settings()

pygame.init()
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))

background_image = pygame.image.load(setting.img_background)


def set_difficulty(value, difficulty):
    # Do the job here !
    print(value, difficulty)
    pass

def set_map(value, difficulty):
    # Do the job here !
    print(value, difficulty)
    pass

def start_the_game():
    # Do the job here !
    screen.blit(background_image, (0, 0))
    manager = Manager()
    manager.create_map()
    manager.create_character(setting)

    while True:
        for event in pygame.event.get():
            event_process(event, manager)

        pygame.display.flip()

def event_process(event, manager):

    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            manager.make_move()

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Player1')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.selector('Map :', setting.maps, onchange=set_map)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
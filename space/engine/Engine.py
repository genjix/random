import pygame

def initialize(app_name, app_version):
    pygame.init()
    pygame.display.set_caption(app_name + ' ' + app_version, '')


def finalize():
    pygame.quit()


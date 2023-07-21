import pygame
from os import walk

def GetChar(path):
    files= []

    for _,__,images in walk(path):
        for image in images:
            dir = path +'\\'+ image
            image_file = pygame.image.load(dir).convert_alpha()
            files.append(image_file)
    return files

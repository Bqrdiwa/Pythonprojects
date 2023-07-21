import pygame
from get_chat import GetChar

# Tile Class
Lavalist=[]
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,type):
        super().__init__()
        self.type = type
        self.pos = pos
        if self.type == 'Grass':
            self.name = 'Grass'
            self.image = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Blocks\main block.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
        if self.type == 'Wood':
            self.name = 'Wood'
            self.image=pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Ground\Block\Wood1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if self.type == 'Large':
            self.name = 'Large'
            self.image = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Blocks\block large.png').convert_alpha()
            self.rect =self.image.get_rect(topleft = pos)
        if self.type == 'Medium_V':
            self.name = 'Med_V'
            self.image = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Blocks\medium_vertical.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if self.type == 'Medium_H':
            self.name = 'Med_H'
            self.image = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Blocks\medium_horizantel.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if self.type == 'Lava':
            self.name = 'Lava'
            self.image_list = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Lavagif')
            self.frame_index =0
            self.frame_speed = 0.11
            self.image = self.image_list[0]
            self.rect = self.image.get_rect(topleft=self.pos)
    def Lava(self,xs):
            self.frame_index += self.frame_speed
            if self.frame_index > 8:
                self.frame_index = 0
            self.image = self.image_list[int(self.frame_index)]
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            self.rect.x += xs
    def update(self,world_speed,world_speed1):
        if self.type != 'Lava':
            self.rect.x += world_speed
            self.rect.y += world_speed1
        if self.type == 'Lava':
            self.Lava(world_speed)

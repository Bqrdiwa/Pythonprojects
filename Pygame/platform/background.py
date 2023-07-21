import pygame
from random import randint
from get_chat import GetChar


class Background(pygame.sprite.Sprite):
    def __init__(self,pos,type,Moreinfo):
        super().__init__()
        self.type = type
        # Define Cloud
        if self.type == 'sky':
            self.player = Moreinfo.sprite
            self.speed= pygame.math.Vector2(0,0)
            self.speed.x = 1
            self.sky_folder= r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Cloud\Squidgame project\\'
            spawnloc = randint(1,3)
            self.image=pygame.image.load(self.sky_folder+('cloud'+str(spawnloc)+'.png'))
            self.rect = self.image.get_rect(topright=pos)
        if self.type == 'grass':
            self.grass_images = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\graphics\decoration\grass')
            self.image = self.grass_images[randint(0,5)]
            self.rect = self.image.get_rect(bottomleft = pos)
        if self.type == 'Tree':
            self.block_type = Moreinfo
            if self.block_type =='Large':
                self.images = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\graphics\terrain\palm_large')
                self.image = self.images[0]
                self.frame_index = 0
                self.frame_speed = 0.09
                self.rect = self.image.get_rect(midbottom= pos)
            if self.block_type =='Small':
                self.images = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\graphics\terrain\palm_small')
                self.image = self.images[0]
                self.frame_index = 0
                self.frame_speed = 0.09
                self.rect = self.image.get_rect(midbottom= pos)
    def spawn_sky(self):
        if self.player.direction.x == -1:
            self.rect.x +=  self.speed.x * 1.2
        else:
            self.rect.x += self.speed.x
    def Tree(self):
        self.frame_index += self.frame_speed
        if self.frame_index > len(self.images):
            self.frame_index = 0
        self.image = self.images[int(self.frame_index)]
    def update(self,wspeed):
        if self.type == 'sky':
            self.spawn_sky()
        if self.type == ('grass'):
            self.rect.x += wspeed
        if self.type == ('Tree'):
            self.Tree()
            self.rect.x += wspeed
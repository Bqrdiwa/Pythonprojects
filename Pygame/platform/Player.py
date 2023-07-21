import pygame
from get_chat import GetChar
# Define player

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # Player animation requirments
        self.pos = pos
        self.images_list=GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Stand')
        self.frame_index = 0
        self.frame_speed = 0.17
        self.image = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Stand\1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.position = 'Stand'
        self.dir = 'Right'
        self.on_ground = False
        self.on_celling = False
        self.on_right = False
        self.on_left = False

        # Player Movements
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 10
        self.speedg= 1
        self.gravity = 0.8
        self.jump_speed = -20
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_ground:
            self.direction.y = self.jump_speed
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.dir = 'Right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.dir = 'Left'
        else:
            self.direction.x = 0
    def Applyg(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y * self.speedg
    def animate(self):
        self.frame_index += self.frame_speed
        if self.frame_index > len(self.images_list):
            self.frame_index = 0
        image = self.images_list[int(self.frame_index)]
        if self.dir == 'Right':
            self.image =image
        if self.dir == 'Left':
            flipped_img =pygame.transform.flip(image,True,False)
            self.image = flipped_img
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom=(self.rect.midbottom))
        elif self.on_celling:

            self.rect = self.image.get_rect(midtop=(self.rect.midtop))


    def PlayerDir(self):
        if self.direction.x == 0 and self.direction.y > 0 and self.direction.y < 1:
            self.images_list = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Stand')
        elif self.direction.y < 0:
            self.images_list = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Jump')
        elif self.direction.y > 1:
            self.images_list = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Fall')
        elif self.direction.x == 1 or self.direction.x == -1:
            self.images_list = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\Player\Run')
    def update(self):
        self.PlayerDir()
        self.animate()
        self.movement()
        self.rect.x += self.direction.x * self.speed




















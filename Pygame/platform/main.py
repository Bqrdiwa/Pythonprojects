import keyboard
import pygame
from setting import *
from tile import *
from level import *
# Setup the screen
pygame.init()
spawnsky_timer = pygame.USEREVENT+1
pygame.time.set_timer(spawnsky_timer, 6000)

screen= pygame.display.set_mode((screen_width,screen_heigh))
clock= pygame.time.Clock()
fps=pygame.font.Font(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Fonts\Pixel.ttf', 40)
Rip_imges =GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\platform\Assets\rip')
image = Rip_imges[0]
img_rect = image.get_rect(center= (screen_width/2,screen_heigh/2-100))
frame_in= 0
frame_sp = 0.3
game_active= 'Active'
level = Level(platform,screen)

# Active game
def RIP():
    global frame_in
    global frame_sp
    global image
    global Rip_imges
    frame_in += frame_sp
    if frame_in > 31:
        frame_in = 0
    return Rip_imges[int(frame_in)]
while True:
    # Pygame Events
    for event in pygame.event.get():
        if game_active == 'Active':
            if event.type == pygame.QUIT:
                quit()
            if event.type == spawnsky_timer:
                level.sky_group()
        else:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level.Restart()
                    game_active ='Active'

    # The Screen Details

    if game_active == 'Active':

        screen.fill('#84ffff')
        if level.Gameactive() == 'Lose':
            game_active = 'Lose'
        level.run()



        clock.tick(60)

        fpss=fps.render('Fps: '+str(int(clock.get_fps())),False,'black')
        screen.blit(fpss,(10,10))

        pygame.display.update()

    else:
        screen.fill('#C0C0C0')
        screen.blit(RIP(),img_rect)

        try_again = fps.render('If You Want To Play Agiain Press Space.',False,'black')
        screen.blit(try_again,(img_rect.x+65,img_rect.bottomleft[1]+50))

        clock.tick(60)
        pygame.display.update()
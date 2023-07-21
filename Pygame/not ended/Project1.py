import pygame
import re
import random
pygame.init()
screen=pygame.display.set_mode((1080,700))
pygame.display.set_caption('project1')
clock=pygame.time.Clock()
pixelfont=pygame.font.Font(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Fonts\Pixel.ttf',40)
background_surface=pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\background\sky2.png').convert()
ground_surface = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Ground\ground_surface.png').convert_alpha()
player_image_stand= pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Player\man1stand.png').convert_alpha()
player_image_walked= pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Player\walkedman1.png').convert_alpha()
mob_creeper_image= pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Mobs\minecraft mobs\creeper2.png').convert_alpha()
mob_creeper_image_explosion= pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Mobs\minecraft mobs\creeper explotion.png').convert_alpha()
explosion=pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Mobs\minecraft mobs\explosion1.png').convert_alpha()
background_surface_blur = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\background\skyblur.png')
zombie_image=pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Mobs\minecraft mobs\zombie.png')
player_image_jumped= pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\Player\manjumped.png').convert_alpha()
zombieroated=pygame.transform.flip(zombie_image,True,False)
gameover = pygame.image.load(r'C:\Users\BrGaMeRxD\Desktop\Python\Pygame\Assets\Images\background\gameover.png')
creeperimgrotated = pygame.transform.flip(mob_creeper_image_explosion,True,False)
player_image_stand=pygame.transform.flip(player_image_stand,True,False)
player_image_walked=pygame.transform.flip(player_image_walked,True,False)
player_image_walked_back=pygame.transform.flip(player_image_walked,True,False)
player_image_stand_back=pygame.transform.flip(player_image_stand,True,False)

zombiwspawn = random.randint(1,2)
exee =0
index = 0
if zombiwspawn == 1:exee=1090
else:exee = -10
zombie=zombie_image.get_rect(topleft=(exee,495))
player_rect_surface=player_image_stand.get_rect(midbottom=(100,546))
ex= random.randint(100,990)
creeper = mob_creeper_image.get_rect(topleft=(ex, -20))
ground_surface_rect = ground_surface.get_rect(topleft=(100,300))
ground_surface_rect1 = ground_surface.get_rect(topleft=(600,240))
playergravity= -20
mobgravity = 0
speed = 3
player_x=0
start=0
moblist=[]
bulletlist=[]
game_active=True
creator =random.randint(1,2)
timertf = pygame.USEREVENT +1
pygame.time.set_timer(timertf,1000)
playeranimation1 = [player_image_stand, player_image_walked]
playeranimation2=[player_image_stand_back,player_image_walked_back]
index2=0
bullet = pygame.Rect(100,100, 10, 10)
def playeranimation(key):
    global index
    global index2
    global test
    global speed
    if key[pygame.K_d]:
        index += 0.1
        if index > len(playeranimation1): index = 0
        player_surf = playeranimation1[int(index)]
        test = 0
        player_rect_surface.x += speed
        return player_surf
    if key[pygame.K_a]:
        test = 1
        index2 += 0.1
        if index2 > len(playeranimation2): index2 = 0
        player_rect_surface.x -= speed
        player_surf = playeranimation2[int(index2)]
        return player_surf
    else:
        if test == 0:
            return player_image_stand
        if test == 1:
            return player_image_stand_back




def randomex():
    creeper.x= random.randint(100, 990)
def ranx():
    rx= random.randint(1,2)
    if rx == 1:
        zombie.x = 1090
    if rx ==2 :
        zombie.x = -10
    return zombie.x

creeperh=20
zombieh =20
test1=0
test=0
playerh=100
while True:
    if game_active == True:
        screen.blit(background_surface, (0, 0))
        screen.blit(ground_surface, ground_surface_rect)
        screen.blit(ground_surface, ground_surface_rect1)
        keypressed = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect_surface.y == 435:
                        playergravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    if speed == 3:
                        speed = 5
                    else:
                        speed = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed()[0]) == True:
                    if test == 0:
                        if player_rect_surface.right < pygame.mouse.get_pos()[0]:
                                if len(bulletlist) > 5:
                                    pass
                                else:
                                    bulletlist.append(pygame.mouse.get_pos())
                    else:
                        if player_rect_surface.left > pygame.mouse.get_pos()[0]:
                            if len(bulletlist) > 5:
                                pass
                            else:
                                bulletlist.append(pygame.mouse.get_pos())

            if event.type == timertf:
                mobslector =random.randint(1,2)
                spawenloc = random.randint(1,2)
                if mobslector in moblist:
                    pass
                else:
                    moblist.append(mobslector)
        else:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = int(pygame.time.get_ticks() / 1000)
                    moblist.clear()
                    ranx()
                    player_rect_surface.x = 100
                    player_rect_surface.y =546
                    playerh = 100
                    game_active = True
    if game_active == True:
        if bulletlist:
            if bulletlist[0][0] > bullet.y:bullet.y +=10
            else:bullet.y -= 10
            if bulletlist[0][0] > bullet.x:bullet.x += 10
            else:bullet.x -= 10







        # Creating mob
        if moblist != []:
            for i in moblist:
                if i == 1:
                    if creeperh <= 0:
                        for i in moblist:
                            if i == 1:
                                moblist.remove(1)
                        creeper.y = -20
                        mobgravity = 0
                        randomex()
                        creeperh = 20
                    if creeper.colliderect(ground_surface_rect) or creeper.y  > 495 or creeper.colliderect(ground_surface_rect1):
                        if creeper.colliderect(player_rect_surface):
                            exlosion =screen.blit(explosion,(creeper.x-40,creeper.y-20))
                            if player_rect_surface.colliderect(exlosion):
                                playerh -= 50
                            for i in moblist:
                                if i == 1:
                                    moblist.remove(1)
                            creeper.y = -20
                            mobgravity = 0
                            randomex()
                            creeperh = 20
                        else:
                            mobgravity = 0
                            if creeper.colliderect(ground_surface_rect) or creeper.colliderect(ground_surface_rect1):
                                    creeper.x += 5
                                    screen.blit(mob_creeper_image_explosion, creeper)
                            elif player_rect_surface.x > creeper.x:
                                creeper.x += 5
                                screen.blit(mob_creeper_image_explosion, creeper)
                            elif player_rect_surface.x < creeper.x:
                                creeper.x -= 5
                                screen.blit(creeperimgrotated, creeper)

                    else:
                        mobgravity += 0.1
                        creeper.y += mobgravity
                        screen.blit(mob_creeper_image, creeper)
                if i == 2:
                    if zombieh <= 0:
                        for i in moblist:
                            if i == 2:
                                moblist.remove(2)
                        zombieh= 30
                        ranx()
                    if zombie.colliderect(player_rect_surface):
                        if random.randint(1,10) ==1 :
                            playerh= playerh- 5
                    if player_rect_surface.x > zombie.x:
                        zombie.x += 3
                        screen.blit(zombie_image, zombie)
                    if player_rect_surface.x < zombie.x:
                        zombie.x -= 3
                        screen.blit(zombieroated, zombie)

        # Ending mobb
        player_surf =playeranimation(keypressed)
        if player_rect_surface.y < 400:
            if test == 0:

                player_surf=pygame.transform.flip(player_image_jumped, True, False)
            else:
                player_surf=player_image_jumped
        screen.blit(player_surf,player_rect_surface)
        if player_rect_surface.y >= 415:
            player_rect_surface.y = 415
        else:
            playergravity += 1
        player_rect_surface.y += playergravity
        text_surface = pixelfont.render('Fps: '+str(int(clock.get_fps())), False, 'Black')
        scoresurface = pixelfont.render(' Score: '+str(int(pygame.time.get_ticks()/1000)- start), False, 'Black')
        screen.blit(text_surface, (10, 10))
        screen.blit(scoresurface,(110,10))
        if playerh <= 20:
            playerhp = pixelfont.render(' Hp: ' + str(playerh), False, 'Red')
            screen.blit(playerhp, (320, 10))
        else:
            playerhp = pixelfont.render(' Hp: ' + str(playerh), False, 'Black')
            screen.blit(playerhp, (320, 10))
        clock.tick(60)
        if playerh <= 0:
            game_active=False
        pygame.display.update()
    else:
        screen.blit(background_surface_blur, (0, 0))
        screen.blit(gameover,(100,100))
        screen.blit(scoresurface, (120, 500))
        pygame.display.update()

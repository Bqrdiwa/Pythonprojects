import random

import pygame
import tile
from setting import *
from Player import *
from background import Background
from random import randint
# Set up the level class

class Level:
    def __init__(self, screen_data, display_surface):
        self.game_active = 'Actice'
        self.display_surface = display_surface
        self.screen_data = screen_data
        self.grass = pygame.sprite.Group()
        self.sky = pygame.sprite.Group()
        self.level_data(screen_data)
        self.wspeed = 0
        self.wspeed1=0
        self.spawnok=False
        self.current_x = 0
    def level_data(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                y = row_index * tile_size
                x = col_index * tile_size
                if col == 'X':
                    self.tiles.add(tile.Tile((x, y),'Large' ))
                    grass_spawn_pos = randint(0,2)*64
                    grass_amount = randint(1,int(3-(grass_spawn_pos/64)))
                    for grass in range(grass_amount):
                        self.grass.add(Background((x+grass_spawn_pos,y),'grass',None))
                        grass_spawn_pos += 64
                    tree_spawn = randint(1,2)
                    tree_type = randint(1,2)
                    if tree_spawn == 1:
                        if tree_type == (1):
                            self.grass.add (Background((x + randint(15,180),y),'Tree','Large'))
                        else:
                            self.grass.add(Background((x + randint(15,180), y), 'Tree', 'Small'))
                    if tree_spawn == 2:
                        xx = randint(15,180)
                        if tree_type == 1:
                            self.grass.add(Background((x + xx, y), 'Tree', 'Small'))
                        else:
                            self.grass.add(Background((x + xx, y), 'Tree', 'Large'))
                        tree_type = randint(1, 2)
                        gen = 0
                        if xx - 40 > 15:
                            gen = 1
                        if xx + 40 < 180:
                            if gen == 1:
                                loop = randint(1,2)
                                if loop == 1:
                                    gen = 1
                                else:
                                    gen = 2
                            else:
                                gen = 2
                        if gen == 1:
                            yy= randint(15,xx-40)
                            if tree_type == 1:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Small'))
                            else:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Large'))
                        else:
                            yy = randint(xx+40,180)
                            if tree_type == 1:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Small'))
                            else:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Large'))
                elif col == 'H':
                    self.tiles.add(tile.Tile((x, y),'Medium_H' ))
                    grass_spawn_pos = randint(0, 2) * 64
                    grass_amount = randint(1, int(3 - (grass_spawn_pos / 64)))
                    for grass in range(grass_amount):
                        self.grass.add(Background((x + grass_spawn_pos, y), 'grass', None))
                        grass_spawn_pos += 64
                    tree_spawn = randint(1, 2)
                    tree_type = randint(1, 2)
                    if tree_spawn == 1:
                        if tree_type == (1):
                            self.grass.add(Background((x + randint(15, 180), y), 'Tree', 'Large'))
                        else:
                            self.grass.add(Background((x + randint(15, 180), y), 'Tree', 'Small'))
                    if tree_spawn == 2:
                        xx = randint(15, 180)
                        if tree_type == 1:
                            self.grass.add(Background((x + xx, y), 'Tree', 'Small'))
                        else:
                            self.grass.add(Background((x + xx, y), 'Tree', 'Large'))
                        tree_type = randint(1, 2)
                        gen = 0
                        if xx - 40 > 15:
                            gen = 1
                        if xx + 40 < 180:
                            if gen == 1:
                                loop = randint(1, 2)
                                if loop == 1:
                                    gen = 1
                                else:
                                    gen = 2
                            else:
                                gen = 2
                        if gen == 1:
                            yy = randint(15, xx - 40)
                            if tree_type == 1:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Small'))
                            else:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Large'))
                        else:
                            yy = randint(xx + 40, 180)
                            if tree_type == 1:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Small'))
                            else:
                                self.grass.add(Background((x + yy, y), 'Tree', 'Large'))
                elif col == 'V':
                    self.tiles.add(tile.Tile((x, y),'Medium_V' ))
                    grass_spawn = randint(1,2)
                    if grass_spawn == 1:
                        self.grass.add(Background((x,y),'grass',None))
                    tree_spawn = randint(1, 2)
                    tree_type = randint(1, 2)
                    if tree_spawn == 1:
                        if tree_type == (1):
                            self.grass.add(Background((x + randint(7, 53), y), 'Tree', 'Large'))
                        else:
                            self.grass.add(Background((x + randint(7, 53), y), 'Tree', 'Small'))
                elif col == 'W':
                    self.tiles.add(tile.Tile((x, y), 'Wood'))
                elif col == 'P':
                    self.player.add(Player((col_index * tile_size,row_index * tile_size)))
                elif col == 'x':
                    self.tiles.add(tile.Tile((x,y),'Grass'))
                    grass_spawn = randint(1, 2)
                    if grass_spawn == 1:
                        self.grass.add(Background((x, y), 'grass', None))
                    tree_spawn = randint(1, 2)
                    tree_type = randint(1, 2)
                    if tree_spawn == 1:
                        if tree_type == (1):
                            self.grass.add(Background((x + randint(7, 53), y), 'Tree', 'Large'))
                        else:
                            self.grass.add(Background((x + randint(7, 53), y), 'Tree', 'Small'))
                elif     col == 'L':
                    self.tiles.add(tile.Tile((x, y), 'Lava'))
    def Show_Screen(self):
        players = self.player.sprite
        player_x = players.rect.centerx
        player_direction = players.direction.x

        if player_x > (screen_width/2)  and player_direction == 1:
            self.wspeed = -5
            players.speed = 0
        elif player_x < screen_width-(screen_width/2) and player_direction == -1:
            self.wspeed = 5
            players.speed = 0
        else:
            self.wspeed = 0
            players.speed = 7
    def collid_x(self):
        player = self.player.sprite
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.x > 0 and player.dir == 'Right' :
                    if player.rect.right > sprite.rect.left+67 and player.on_celling == False:
                        player.rect.bottomleft= sprite.rect.bottomright
                    else:
                        player.direction.x =0
                        player.on_right=True
                        player.rect.right = sprite.rect.left
                        self.current_x = player.rect.right
                elif player.direction.x < 0 and player.dir == 'Left':
                    if player.rect.left < sprite.rect.right-67 and player.on_celling == False:
                        player.rect.bottomright = sprite.rect.bottomleft
                    else:
                        player.direction.x = 0
                        player.on_left = True
                        player.rect.left = sprite.rect.right
                        self.current_x = player.rect.left
            if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
                player.on_right = False
            if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
                player.on_left = False
    def collid_y(self):
        player = self.player.sprite
        player.Applyg()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0 :
                    player.direction.y = 0
                    player.on_ground = True
                    player.rect.bottom = sprite.rect.top

                elif player.direction.y < 0:
                    player.on_celling =True
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                if sprite.name == 'Lava':
                    self.game_active = 'Lose'
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_celling and player.direction.y < 1:
            player.on_celling = False
        if player.rect.y > 1000:
            self.game_active = 'Lose'


    def sky_group(self):
        if len(self.sky.sprites()) > 5:
            for sprite in self.sky.sprites():
                if sprite.rect.x > screen_width + 100:
                    self.sky.remove(sprite)
        self.sky_pos = (-20,randint(10,200))
        self.sky.add(Background(self.sky_pos, 'sky', self.player))
    def Gameactive(self):
        return self.game_active
    def Restart(self):
        self.game_active = 'Active'
        self.grass.empty()
        self.sky.empty()
        self.level_data(self.screen_data)
    def run(self):

        # Background
        self.sky.update(self.wspeed)
        self.sky.draw(self.display_surface)

        self.grass.update(self.wspeed)
        self.grass.draw(self.display_surface)


        # Showing the Tiles
        self.tiles.update(self.wspeed, self.wspeed1)
        self.tiles.draw(self.display_surface)


        # Player Showing
        self.player.update()
        self.collid_x()
        self.collid_y()
        self.player.draw(self.display_surface)










        # Screen
        self.Show_Screen()
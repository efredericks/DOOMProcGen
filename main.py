##
# Based on: https://www.youtube.com/watch?v=ECqUrT7IdqQ
# Creating a DOOM-style 3D Game in Python from Scratch. Pygame Tutorial
##

## Attempting to use procedural generation to create environments based on the raycasting tutorial
## Erik Fredericks, 2022

import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.minimap_active = False
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        # self.static_sprite = SpriteObject(self)
        # self.animated_sprite = AnimatedSprite(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : 0.1f}')

    def draw(self):

        if self.minimap_active:
            self.screen.fill('black')
            self.map.draw()
            self.player.draw()
        else:
            self.object_renderer.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYUP and event.key == pg.K_TAB:
                self.minimap_active = not self.minimap_active

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
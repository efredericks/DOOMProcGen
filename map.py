import pygame as pg
import opensimplex
from settings import *

_ = False
mini_map = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
  [1, _, _, 3, 3, 3, 3, _, _, _, 1, 1, 1, _, _, 1],
  [1, _, _, _, _, _, 2, _, _, _, _, _, 1, _, _, 1],
  [1, _, _, _, _, _, 2, _, _, _, _, _, 1, _, _, 1],
  [1, _, _, 3, 3, 3, 3, _, _, _, _, _, 1, _, _, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.mini_map = self.generateMap()#mini_map
        self.world_map = {}
        self.get_map()

    def generateMap(self):
        mm = []
        
        for r in range(NUM_ROWS):
            mm.append([])
            for c in range(NUM_COLS):
                if c == 0 or c == NUM_COLS-1 or r == 0 or r == NUM_COLS:
                    mm[r].append(1)
                else:
                    n = opensimplex.noise2(c * NOISE_ZOOM, r * NOISE_ZOOM)
                    if n < 0.0:
                        spr = _
                    else:
                        spr = int(p5Map(n, 0.0, 1.0, 1, 5))
                    mm[r].append(spr)
        return mm
        # return mini_map

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]


#/usr/bin/env python
import os, pygame
from map import *
from pygame.locals import *
from shapely.geometry import Point, Polygon
from colors import random_color

class Gui(object):
    def __init__(self):
        self.screen = None
        self.foreground = None
        self.background = None
        self.width = 1440
        self.height = 960
        self.caption = '2040'

    def _prepare(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        pygame.mouse.set_visible(1)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.foreground = pygame.Surface(self.screen.get_size())

    def _draw_map(self):
        map = UsaMap()
        for points in map.get_map():
            pygame.draw.polygon(self.foreground, random_color("blue"), points)

    def _blit(self):
        self.screen.blit(self.background, (0, 0))
        self.background.blit(self.foreground, (0, 0))
        pygame.display.flip()

    def load_gfx(self):
        self._prepare()
        self._draw_map()
        self._blit()

    def game_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    return

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()


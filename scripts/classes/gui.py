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
        color1 = random_color("red")
        color2 = random_color("blue")
        #TODO: These maps don't need to be separate class objects
        usa_map = UsaMap()
        china_map = ChinaMap()
        for points in china_map.get_map():
            if len(points) > 2:
                pygame.draw.polygon(self.foreground, color1, points)
        for points in usa_map.get_map():
            if len(points) > 2:
                pygame.draw.polygon(self.foreground, color2, points)
        #self._create_regions(china_map, usa_map)

    def _create_regions(self, map1, map2):
        #loop through map points and draw with 1 color n polygons that touch
        #keep looping till polygon is drawn
        prev_points = None
        n = 0
        pointz = map1.get_map()
        for points in pointz:
            if len(points) > 2:
                pt = Point(points)
                if prev_points is not None:
                    if pt.touches(prev_points) and n < 8:
                        print "touching"
                        color1 = random_color("red")
                        pygame.draw.polygon(self.foreground, color1, points)
                        prev_points = Point(points)
                        n += 1
                    else:
                        n = 0
                else:
                    prev_points = Point(points)


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


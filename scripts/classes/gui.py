#/usr/bin/env python
import os, pygame
from map import *
from pygame.locals import *
from shapely.geometry import Point, Polygon
from colors import random_color, search_color
from pprint import pprint

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

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
        china_regions = []
        usa_regions = []
        color1 = search_color("red")
        color2 = search_color("blue")
        #TODO: These maps don't need to be separate class objects
        usa_map = UsaMap()
        china_map = ChinaMap()
        china_regions = china_map.get_map()
        for points in china_regions:
            if len(points.values()[0]) > 2:
                pygame.draw.polygon(self.foreground, hex_to_rgb("a80000"), points.values()[0])
        #get regions w/ proper polygons
        self.usa_regions = [x for x in usa_map.get_map() if len(x.values()[0]) > 2]
        for points in self.usa_regions:
            if len(points.values()[0]) > 2:
                pygame.draw.polygon(self.foreground, hex_to_rgb("0052a5"), points.values()[0])


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
                    from pprint import pprint
                    pt = Point(pygame.mouse.get_pos())
                    pt_match = [[key for key,val in x.iteritems() if pt.intersects(Polygon(val))] for x in self.usa_regions]
                    #pt_match = [value for key,value in self.usa_regions[0] if pt.intersects(value)]
                    #pt_match = [a for a in self.usa_polys if pt.intersects(Polygon(a))]
                    if pt_match:
                        #clear out the empty lists so that pt_match only contains the region string
                        pt_match = [x for x in pt_match if x]
                        pprint(pt_match[0][0])


            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()


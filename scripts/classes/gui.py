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
        self.world = World()

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
        #TODO: These maps don't need to be separate class objects
        usa_map = UsaMap()
        china_map = ChinaMap()

        #get the china map but make sure they are polygons
        self.china_regions = ([x for x in china_map.get_map()
        if len(x.values()[0]) > 2])

        #draw the china map
        for points in self.china_regions:
            (pygame.draw.polygon(self.foreground, hex_to_rgb("a80000"),
            points.values()[0]))

        #get the usa map but make sure they are polygons
        self.usa_regions = ([x for x in usa_map.get_map()
        if len(x.values()[0]) > 2])

        #draw the usa mao
        for points in self.usa_regions:
            (pygame.draw.polygon(self.foreground, hex_to_rgb("0052a5"),
            points.values()[0]))

        self.all_regions = self.china_regions + self.usa_regions


    def _blit(self):
        self.screen.blit(self.background, (0, 0))
        self.background.blit(self.foreground, (0, 0))
        pygame.display.flip()

    def load_gfx(self):
        self._prepare()
        self._draw_map()
        self._blit()

    def click(self, clicked):
        if clicked > 4 < 7:
            controller.click(clicked)

    def game_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    pt = Point(pygame.mouse.get_pos())

                    #this list comprehension gets the clicked region
                    pt_match = ([[key for key,val in regns.iteritems()
                    if pt.intersects(Polygon(val))] for regns in self.all_regions])

                    if pt_match:
                        #clear out the empty lists so that pt_match
                        #only contains the region string
                        pt_match = [match for match in pt_match if match]
                        try:
                            #send click info to the world object
                            self.world.process_action(pt_match[0][0])
                        except IndexError:
                            pass



            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()


#!/usr/bin/env python
import os, pygame
import world_funcs as _world
import map_funcs as _map
from misc_funcs import hex_to_rgb
from map import *
from pygame.locals import *
from shapely.geometry import Point, Polygon
from colors import random_color, search_color
from pprint import pprint

WIDTH = 1440
HEIGHT = 960
CAPTION = '2040'

def make_gui():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.mouse.set_visible(1)
    background = pygame.Surface(self.screen.get_size())
    background = self.background.convert()
    background.fill((250, 250, 250))
    foreground = pygame.Surface(self.screen.get_size())
    draw_map(pygame, foreground)
    screen.blit(self.background, (0, 0))
    background.blit(self.foreground, (0, 0))
    pygame.display.flip()


def draw_map():
    #get the china map but make sure they are polygons
    china_regions = ([x for x in _map.get_map(1)
    if len(x.values()[0]) > 2])

    #draw the china map
    for points in china_regions:
        (pygame.draw.polygon(foreground, hex_to_rgb("a80000"),
        points.values()[0]))

    #get the usa map but make sure they are polygons
    usa_regions = ([x for x in _map.get_map(0)
    if len(x.values()[0]) > 2])

    #draw the usa mao
    for points in usa_regions:
        (pygame.draw.polygon(foreground, hex_to_rgb("0052a5"),
        points.values()[0]))

    all_regions = china_regions + usa_regions

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
                if pt.intersects(Polygon(val))] for regns in all_regions])

                if pt_match:
                    #clear out the empty lists so that pt_match
                    #only contains the region string
                    pt_match = [match for match in pt_match if match]
                    try:
                        #send click info to the world object
                        _world.process_action(world, pt_match[0][0])
                    except IndexError:
                        pass



        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


def main():
    try make_gui():
        world = _world.make_world()
        game_loop()
    except:
        pass

if __name__ == '__main__': main()

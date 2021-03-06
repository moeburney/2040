#!/usr/bin/env python
import os, pygame
import world_funcs as _world
import map_funcs as _map
from misc_funcs import hex_to_rgb
from pygame.locals import *
from shapely.geometry import Point, Polygon
#todo: change directory structure
from scripts.classes.colors import random_color, search_color
from pprint import pprint

WIDTH = 1440
HEIGHT = 960
CAPTION = '2040'

def make_gui():
    pygame.init()
    #todo: figure out a way to not use global
    global screen
    global background
    global foreground
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    foreground = pygame.Surface(screen.get_size())
    draw_map(foreground)
    screen.blit(background, (0, 0))
    background.blit(foreground, (0, 0))
    pygame.display.flip()


def draw_map(foreground):
    #get the china map but make sure they are polygons
    global china_regions
    global usa_regions
    china_regions = ([x for x in _map.get_map(1)
    if len(x.values()[0]) > 2])

    #draw the china map
    for points in china_regions:
        (pygame.draw.polygon(foreground, hex_to_rgb("a80000"),
        points.values()[0]))

    #get the usa map but make sure they are polygons
    usa_regions = ([x for x in _map.get_map(0)
    if len(x.values()[0]) > 2])

    #draw the usa map
    for points in usa_regions:
        (pygame.draw.polygon(foreground, hex_to_rgb("0052a5"),
        points.values()[0]))

    #todo: don't use global
    global all_regions
    all_regions = china_regions + usa_regions

def color_regions(world):
    global foreground
    global all_regions
    for points in all_regions:
        if points.keys()[0] in world["players"][0]["regions"]:
            pygame.draw.polygon(foreground, hex_to_rgb("0052a5"), points.values()[0])
        if points.keys()[0] in world["players"][1]["regions"]:
            pygame.draw.polygon(foreground, hex_to_rgb("a80000"), points.values()[0])

def game_loop():
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
                    #player clicked a region, coords are in nested list
                    #clear out the empty lists so that pt_match
                    #only contains the region int
                    pt_match = [match for match in pt_match if match]
                    try:
                        pt_int = pt_match[0][0]
                        print "state is "
                        print pt_int
                    except IndexError:
                        pt_int = 14
                else:
                    #player clicked outside of a region
                    pt_int = 15

                #send click info to the world object
                global world
                world = _world.process_action(world, pt_int)
                world = _world.refresh(world)
                color_regions(world)
                '''
                if world['end'] == 1:
                    print "Game over."
                    return
                '''

        background.blit(foreground, (0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.display.update()


def main():
    #todo: error handling
    make_gui()
    #todo: don't use global
    global world
    world = _world.make_world()
    game_loop()

if __name__ == '__main__': main()

'''
Created on Jul 14, 2011
@file: colors.py
@author: jake bolton

Usage:
    Feel free to use code as you want!
    
functions:
    random_color(search=None):
    search_color(name)
'''
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
from random import choice

VERSION = '0.1'

# 
def random_color(search=None):
    """get a single random Color(), with Optional search filter.
        search='green' will return 'seagreen', 'bluegreen', etc...
        
    default to choice() of full list"""    
    if search: c = choice(search_color(search))
    else: c = choice(THECOLORS.values())
    
    #debug: print type(c), c # returns Color()
    return c 
    #todo: exception on color search fail? OR just default to white.

def search_color(name):
    """search pygame. THECOLORS for a name, example:
        "green" -> seagreen, bluegreen, darkgreen
    """
    #verbose:    print "search_color( {} ) =".format(name)
    return [Color(c) for c in pygame.color.THECOLORS if name in c]

# for search*
color_groups = ['', 'white', 'purple','green','dark','light','red','blue','orange','gray','blue','green']    
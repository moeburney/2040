#!/usr/bin/env python

'''in this module, each function modifies elements of the world
by calling functions in the game_functions module'''

import game_funcs as _game

def make_world():
    world = {}
    world['players'] = _game.make_players()
    world['end'] = 0
    return world

def process_action(world, action):
    '''the circuit board for all inputs'''
    print action
    players = world['players']
    player_n = _game.get_active_player(world)

    if action < 8:
        player = _game.attack(players, action)
        print "attacked"
    else:
        player = _game.invest(world['players'][player_n])
        print "invested"

    print world
    return world

def refresh(world):
    player_n = _game.get_active_player(world)
    if len(world['players'][player_n]["regions"]) < 1:
        world['end'] = 1
    else:
        world['players'] = _game.swap_turns(world['players'])
    return world






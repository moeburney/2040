#!/usr/bin/env python

'''in this module, each function modifies elements of the world
by calling functions in the game_functions module'''

import game_funcs as _game

def make_world():
    world = {}
    world['players'] = _game.make_players(2)
    world['end'] = 0
    return world

def process_action(world, action):
    '''the circuit board for all inputs'''
    players = world['players']
    player_n = _game.get_active_player(world)

    if action > 1 < 8:
        player = _game.attack(players, world['players'][player_n], action)
    elif action > 8 or action is None:
        player = _game.invest(world['players'][player_n])
        print "invested"

    #awkward line needs fixing
    return world

def refresh(world):
    player_n = _game.get_active_player(world)
    if len(world['players'][player_n][regions]) < 1:
        world['end'] = 1
    else:
        world['players'] = _g.swap_turns(world['players'])
    return world






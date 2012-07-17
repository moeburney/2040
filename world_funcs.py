#/usr/bin/env python

'''in this module, each function modifies elements of the world
by calling functions in the game_functions module'''

import game_funcs as _game

def make_world():
    world = {}
    world['players'] = _game.make_players()
    world['end'] = 0
    return world

def process_action(self, world, action):
    '''the circuit board for all inputs'''
    player = _game.get_active_player(world)

    if action > 1 < 8:
        player = _game.attack(player, region)
    elif action > 8 or action is None:
        player = _game.invest(player)
        print "invested"

    #awkward line needs fixing
    world['players'][player] = player
    return world

def refresh(world):
    if len(_game.get_active_player(world)[regions]) < 1:
        world['end'] = 1
    else:
        world['players'] = _g.swap_turns(world['players'])
    return world






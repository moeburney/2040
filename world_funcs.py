#/usr/bin/env python

'''in this module, each function modifies elements of the world
by calling functions in the game_functions module'''

import game_funcs as _game

def make_world():
    world = {}
    world['players'] = _game.make_players()
    return world

def process_action(self, world, action):
    player = _game.get_active_player(world)

    if action > 1 < 8:
        player = _game.attack(player, region)
    elif action > 8:
        player = _game.invest(player)

    return world

def refresh(world):
    if len(_game.get_active_player(world)[regions]) < 1:
        world['active'] = 0
    else:
        world['active'] = _game.swap_turns(world)
    return world






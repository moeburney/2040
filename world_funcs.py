#/usr/bin/env python
import game_funcs as _game

def make_world():
    world = {}
    world['players'] = _game.make_players()
    return world

def process_action(self, world, action):
    player = _game.get_active_player(world)

    if action > 1 < 5:
        _game.attack(player, region)
    elif action > 5:
        _game.build(player, region)

    _game.refresh_world(world)

def refresh_world(self, world):
    if _game.get_active_player(world)[points] > 100:
        _game.end_game()
    else:
        _game.swap_turns()





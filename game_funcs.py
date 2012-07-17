#/usr/bin/env/python

def make_players(n, players=None):
    if players is None:
        players = []
    if n < 2:
        players[n] = ({"points": 0,
                       "morale":0,
                       "prestige":0,
                       "cash":0,
                       "power":0,
                       "regions":[],
                       "active":0,
                       "country":n})
        n+= 1
        return make_players(n, players)
    else:
        return players

def attack(players, region):
    # a very rudimentary combat game logic
    for n in players:
        if n["active"] == 1:
            attacker = player[n]
        if region is in n["region"]:
            defender = player[n]

    if attacker["morale"] > defender["morale"]:
        return conquer(attacker, region)

def invest(player):
    #returns a random tech investment
    investment = _random_invest()
    player['morale'] += investment['points']
    return player

def conquer(attacker, defender, region):
    attacker["regions"].append(region)
    defender["regions"].remove(region)
    return player

def get_active_player(world):
    if world['players'][0]['active'] == 1:
        return 0
    else:
        return 1

def swap_turns(players):
    #todo: make this simpler
    if players[0]['active'] == 1:
        players[0]['active'] = 0
        players[1]['active'] = 1
    elif players[1]['active'] == 1:
        players[1]['active'] = 0
        players[0]['active'] = 1
    else:
        print "both players are inactive"

def _random_invest():
    '''very simple first version'''
    from random import randint
    return randint(1, 100)

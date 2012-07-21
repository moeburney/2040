#/usr/bin/env/python
def make_players(n=0, players=None):
    if players is None:
        players = []
        players.append({})
        players.append({})
    #todo: make this clearer
    if n == 0:
        region_range = xrange(1, 7)
        active = 1
        morale = 20000
    elif n == 1:
        region_range = xrange(7, 13)
        active = 0
        morale = 0
    if n < 2:
        players[n] = ({"points": 0,
                       "morale":morale,
                       "prestige":0,
                       "cash":0,
                       "power":0,
                       "regions":list(region_range),
                       "active":active,
                       "country":n})
        n += 1
        return make_players(n, players)
    else:
        return players

def attack(players, region):
    # a very rudimentary combat game logic
    for n in xrange(2):
        if players[n]["active"] == 1:
            attacker = n
        if region in players[n]["regions"]:
            defender = n

    if 'defender' not in locals():
        return

    if players[attacker]["morale"] > players[defender]["morale"]:
        return conquer(players, attacker, defender, region)

def invest(player):
    #returns a random tech investment
    investment = _random_invest()
    player['morale'] += investment
    return player

def conquer(players, attacker, defender, region):
    players[attacker]["regions"].append(region)
    players[defender]["regions"].remove(region)
    return players

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
    return players

def _random_invest():
    '''very simple first version'''
    from random import randint
    return randint(1, 100)

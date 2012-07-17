#/usr/bin/env/python

def make_players():
    players = {}
    for n in range(2):
        players[n] = ({"points": 0,
                       "morale":0,
                       "prestige":0,
                       "cash":0,
                       "power":0,
                       "regions":[],
                       "country":n})
    return players

def attack(player, region):
    enemy = get_owner(region)
    if player is enemy:
        pass
    # a very rudimentary rule to win
    if player["morale"] > enemy["morale"]:
        conquer(player, region)

def get_owner(region):
    pass

def invest(player):
    #returns a random tech investment
    investment = _random_invest()
    player['points'] += investment['points']
    return player

def conquer(player, region):
    player["regions"].append(region)

def get_active_player(world):
    if world['players'][0]['active'] == 1:
        return world['players'][0]
    else:
        return world['players'][1]


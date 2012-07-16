#/usr/bin/env/python

def make_players():
    players = {}
    for n in range(2):
        players[n] = ({"points": 0,
                       "morale":0,
                       "prestige":0,
                       "cash":0,
                       "power":0,
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

def conquer(player, region):
    player["regions"].append(region)

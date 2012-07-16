#/usr/bin/env python
from player import Player

class World(object):
'''A singleton world class'''
    def __init__(self):
        countries = [1 , 2]
        player1 = Player(1)
        player2 = Player(2)
        active_plyr = player1
        waiting_plyr = player2

    def process_action(self, action):
        if action == 5 or > 1 < 3:
            self.active_plyr.attack(region)
        elif action == 10:
            self.active_plyr.build(item)
        self.refresh_world()

    def refresh_world(self):
        if self.active_plyr.won():
            self.end_game()
        else:
            #swap player turns
            (self.active_plyr, self.waiting_plyr =
            self.waiting_plyr, self.active_plyr)





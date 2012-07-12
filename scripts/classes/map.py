#!/usr/bin/env python

from scripts.parse_svg import parse

class Map(object):
    def __init__(self):
        self.image = None
        self.x = 800
        self.y = 600
        self.width_ratio = 0.75
        self.height_ratio = 0.75
        self.start_pos = 0

    def _convert_state_to_region(self, state):
        if (state in ["WA", "CA", "OR", "NV", "MT", "ID", "WY", "UT", "CO",
            "AZ", "NM"]):
            return 1
        elif (state in ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "IL",
            "IN", "MI", "OH"]):
            return 2
        elif (state in ["OK", "TX", "AR", "LA", "KY", "TN", "MS", "AL", "WV",
            "MD", "DE", "DC", "VA", "NC", "SC", "MS", "AL", "GA", "FL"]):
            return 3
        elif (state in ["NY", "PA", "NJ", "VT", "NH", "ME", "MA", "CT", "RI",
            "NJ"]):
            return 4
        elif state in ["_40446064", "_40521872", "_40437568"]:
            return 5
        else:
            return 6

    def _svg_to_polygons(self):
        """Converts the svg map file to a list of polygons"""
        polygons = []
        groups = parse(self.image)

        #iterating this dict in a strange way, need to refactor maybe
        for g in groups:
            for path in groups[g]:
                points = [(p[0]*self.width_ratio + self.start_pos, p[1]*self.height_ratio) for p in path[1]]
                polygons.append({self._convert_state_to_region(g):points})

        return polygons

    def get_map(self):
        return self._svg_to_polygons()

class UsaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.image = './gfx/map_usa.svg'
        self.start_pos = 10

class ChinaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.width_ratio = 1
        self.height_ratio = 1
        self.image = './gfx/map_china.svg'
        self.start_pos = 780



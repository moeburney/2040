#!/usr/bin/env python

from scripts.parse_svg import parse


class Map(object):
    def __init__(self):
        self.image = None
        self.x = 800
        self.y = 600
        self.width_ratio = 0.75
        self.height_ratio = 0.75

    def _svg_to_polygons(self):
        """Converts the svg map file to a list of polygons"""
        polygons = []
        groups = parse(self.image)

        for g in groups:
            for path in groups[g]:
                points = [(p[0]*self.width_ratio, p[1]*self.height_ratio) for p in path[1]]
                polygons.append(points)

        return polygons

    def get_map(self):
        return self._svg_to_polygons()

class UsaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.image = './gfx/map_usa.svg'

class ChinaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.image = './gfx/map_china.svg'



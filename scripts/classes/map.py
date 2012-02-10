#!/usr/bin/env python

from scripts.parse_svg import parse
from scripts.parse_china import parse as parse_china


class Map(object):
    def __init__(self):
        self.image = None
        self.keyword = None
        self.x = 800
        self.y = 600
        self.width_ratio = 0.75
        self.height_ratio = 0.75
        self.start_pos = 0

    def _svg_to_polygons(self):
        """Converts the svg map file to a list of polygons"""
        polygons = []
        groups = parse(self.image, self.keyword)

        for g in groups:
            for path in groups[g]:
                points = [(p[0]*self.width_ratio + self.start_pos, p[1]*self.height_ratio) for p in path[1]]
                polygons.append(points)

        return polygons

    def get_map(self):
        return self._svg_to_polygons()

class UsaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.image = './gfx/map_usa.svg'
        self.keyword = 'States'
        self.start_pos = 10

class ChinaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.width_ratio = 1
        self.height_ratio = 1
        self.image = './gfx/map_china.svg'
        self.keyword = None
        self.start_pos = 780



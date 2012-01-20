#!/usr/bin/env python

from scripts.parse_svg import parse


class Map(object):
    def __init__(self):
        self.image = None
        self.x = 800
        self.y = 600
        self.width_ratio = 1
        self.height_ratio = 1

    def _get_region_coords(self, region):
        """Returns the coords for a region"""
        return [(r[0] * self.width_ratio, r[0] * self.height_ratio) for r in region[1]]

    def _svg_to_polygon(self):
        """Converts the svg map file to a list of polygons"""
        groups = parse(self.image)
        polygons = [[self._get_region_coords(region) for region in g] for g in groups]
        return polygons

    def get_map(self):
        return self._svg_to_polygon()

class UsaMap(Map):
    def __init__(self):
        self.image = './gfx/maps/usa.svg'

class ChinaMap(Map):
    def __init__(self):
        pass



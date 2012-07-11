"""
This script parses an svg and returns a list of coords
Originally based on an svg to html script written by David Lynch
"""

import re
import sys
import xml.dom.minidom

import parse_path


def parse(filename):

    svg_file = xml.dom.minidom.parse(filename)

    svg = svg_file.getElementsByTagName('svg')[0]

    x, y = 800, 600

    width = svg.getAttribute('width')
    height = svg.getAttribute('height')

    raw_width = float(width)
    raw_height = float(height)

    width_ratio = x and (x / raw_width) or 1
    height_ratio = y and (y / raw_height) or 1
    elements = [g for g in svg.getElementsByTagName('g') if (g.hasAttribute('id'))]
    elements.extend([p for p in svg.getElementsByTagName('path') if (p.hasAttribute('id'))])


    parsed_groups = {}
    colors = {}
    for e in elements:
        color = e.getAttribute('style')[6:12]
        paths = []
        points = parse_path.get_points(e.getAttribute('d'))
        for pointset in points:
            paths.append([e.getAttribute('id'), pointset])
        parsed_groups[e.getAttribute('id')] = paths
        colors[e.getAttribute('id')] = color

    return parsed_groups




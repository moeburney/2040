"""
This script converts a subset of SVG into an HTML imagemap

Note *subset*.  It only handles <path> elements, for which it only pays
attention to the M and L commands.  Futher, it only notices the "translate"
transform.

It was written to generate the examples in the documentation for maphilight,
and thus is very squarely aimed at handling several SVG maps from wikipedia.
It *assumes* that all the <path>s it will need are inside a <g>.  Any <path>
outside of a <g> will be ignored.

It takes several possible arguments, in the form:
$ svn2imagemap.py FILENAME [x y [group1 group2 ... groupN]]

FILENAME must be the name of an SVG file.  All other arguments are optional.

x and y, if present, are the dimensions of the image you'll be creating from
the SVG.  If not present, it assumes the values of the width and height
attributes in the SVG file.

group1 through groupN are group ids.  If only want particular groups used,
enter their ids here and all others will be ignored.
"""

import re
import sys
import xml.dom.minidom

import parse_path


def parse(filename):



    svg_file = xml.dom.minidom.parse(filename)

    svg = svg_file.getElementsByTagName('svg')[0]

    x, y = 800, 600
    #x , y = None, None
    groups = 'States'
    #groups = None


    width = svg.getAttribute('width')
    height = svg.getAttribute('height')
    #width, height = 958.691, 592.79

    raw_width = float(width)
    raw_height = float(height)

    width_ratio = x and (x / raw_width) or 1
    height_ratio = y and (y / raw_height) or 1


    if groups:
        elements = [g for g in svg.getElementsByTagName('g') if (g.hasAttribute('id') and g.getAttribute('id') in groups)]
        elements.extend([p for p in svg.getElementsByTagName('path') if (p.hasAttribute('id') and p.getAttribute('id') in groups)])
    else:
        elements = svg.getElementsByTagName('g')

    parsed_groups = {}
    for e in elements:
        paths = []
        if e.nodeName == 'g':
            for path in e.getElementsByTagName('path'):
                points = parse_path.get_points(path.getAttribute('d'))
                #print points
                #points = path.getAttribute('d')
                for pointset in points:
                    paths.append([path.getAttribute('id'), pointset])
        else:
            points = parse_path.get_points(e.getAttribute('d'))
            for pointset in points:
                paths.append([e.getAttribute('id'), pointset])
        if e.hasAttribute('transform'):
            #print e.getAttribute('id'), e.getAttribute('transform')
            for transform in re.findall(r'(\w+)\((-?\d+.?\d*),(-?\d+.?\d*)\)', e.getAttribute('transform')):
                if transform[0] == 'translate':
                    x_shift = float(transform[1])
                    y_shift = float(transform[2])
                    for path in paths:
                        path[1] = [(p[0] + x_shift, p[1] + y_shift) for p in path[1]]
        parsed_groups[e.getAttribute('id')] = paths

    return parsed_groups



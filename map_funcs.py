#!/usr/bin/env python

#todo: change the dir structure
from scripts.classes.scripts.parse_svg import parse

USA_DATA = ({"image":'./gfx/map_usa.svg',
             "width":800,
             "height":600,
             "width_ratio":0.75,
             "height_ratio":0.75,
             "start_pos":0})


CHINA_DATA = ({"image":'./gfx/map_china.svg',
               "width":800,
               "height":600,
               "width_ratio":0.75,
               "height_ratio":0.75,
               "start_pos":780})

def _convert_state_to_region(state):
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

def _svg_to_polygons(cdata):
    """Converts the svg map file to a list of polygons"""
    polygons = []
    groups = parse(cdata['image'])

    #iterating this dict in a strange way, need to refactor maybe
    for g in groups:
        for path in groups[g]:
            #this list comprehension gets the region coordinates
            points = ([(p[0] * cdata['width_ratio'] + cdata['start_pos'], p[1]
            * cdata['height_ratio']) for p in path[1]])

            polygons.append({_convert_state_to_region(g):points})

    return polygons

def get_map(country):
    if country == 0:
        cdata = USA_DATA
    else:
        cdata = CHINA_DATA
    return _svg_to_polygons(cdata)




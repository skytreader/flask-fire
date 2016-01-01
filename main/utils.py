import main
import re


def route_exists(route):
    return route in map(lambda r: r.rule, main.main.url_map.iter_rules())

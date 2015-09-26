import app
import re


def route_exists(route):
    return route in map(lambda r: r.rule, app.app.url_map.iter_rules())

import math

def round_result(value, precision):
    return round(value, precision)

def convert_to_radians(angle, unit='radian'):
    if unit == 'degree':
        return math.radians(angle)
    return angle
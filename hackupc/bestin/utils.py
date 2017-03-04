import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'E' or direction == 'N':
        dd *= -1
    return dd;

def convert_degs_to_decimal(deg_str):
    splits = re.split('[ °\'"]+', deg_str)
    lat = dms2dd(splits[1], splits[2], splits[3], splits[0])
    lon = dms2dd(splits[6], splits[7], splits[8], splits[5])
    return [lat, lon]

def value(colors):
    color_code = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    color_value = ""
    for color in colors:
        color_value += str(color_code.get(color))

    return int(color_value[:2])
    
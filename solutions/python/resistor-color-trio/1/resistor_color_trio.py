def label(colors):
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

    suffix = {
        9: " gigaohms",
        6: " megaohms",
        3: " kiloohms"
    }
    
    value = ""
    for color in colors[:2]:
        value += str(color_code.get(color))

    multiplier = color_code.get(colors[2])
    value = str(int(value) * (10 ** multiplier))
    
    zero_count = value.count("0")
    if zero_count not in suffix.keys():
        zero_count -= 1
        
    value_suffix = suffix.get(zero_count, "")
    if value_suffix:
        value = value.replace("0", "", zero_count) + value_suffix
    else:
        value += " ohms"
    
    return value
    
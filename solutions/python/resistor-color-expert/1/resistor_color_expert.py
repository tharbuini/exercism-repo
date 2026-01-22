def resistor_label(colors):
    color_code = {
        "black":  "0",
        "brown":  "1",
        "red":    "2",
        "orange": "3",
        "yellow": "4",
        "green":  "5",
        "blue":   "6",
        "violet": "7",
        "grey":   "8",
        "white":  "9"
    }

    tolerance_band = {
        "grey":   " ±0.05%",
        "violet": " ±0.1%",
        "blue":   " ±0.25%",
        "green":  " ±0.5%",
        "brown":  " ±1%",
        "red":    " ±2%",
        "gold":   " ±5%",
        "silver": " ±10%"
    }

    suffix = {
        9: " gigaohms",
        6: " megaohms",
        3: " kiloohms"
    }

    resistance_value = ""
    
    # Limiting max resistance bands
    resistor_bands = len(colors) - 1
    if resistor_bands > 4:
        resistor_bands = 4
        
    # Treating the case where there is only one color
    if resistor_bands:    
        resistances = colors[0:resistor_bands - 1]
        multiplier = int(color_code.get(colors[resistor_bands - 1], "0"))
        tolerance = tolerance_band.get(colors[resistor_bands], "")
    else:
        resistances = colors
        multiplier = 1
        tolerance = ""

    for resistance_color in resistances:
        resistance_value += color_code.get(resistance_color, "")

    resistance_value = str(int(resistance_value) * (10 ** multiplier))
    
    zero_count = resistance_value.count("0")
    if zero_count not in suffix.keys():
        zero_count -= 1

    value = int(resistance_value)
    for exponent in [3, 6, 9]:
        division = value / (10 ** exponent)
        if (division >= 1) and (0 < division < 100):
            if division.is_integer():
                division = int(division)
                
            resistance_value = str(division)
            zero_count = exponent
        
    resistance_value += suffix.get(zero_count, " ohms")
    resistance_value += tolerance
    
    return resistance_value

def line_up(name, number):
    map = {
        "1": "st",
        "2": "nd",
        "3": "rd"
    }
    
    if str(number)[-2:] in ["11", "12", "13"]:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
    else:
        return f"{name}, you are the {number}{map.get(str(number)[-1], 'th')} customer we serve today. Thank you!"
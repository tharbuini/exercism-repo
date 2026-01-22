def commands(binary_str):
    actions = {
        0: "wink",
        1: "double blink",
        2: "close your eyes",
        3: "jump",
        4: "reverse"
    }

    actions_list = []
    for index, character in enumerate(binary_str[::-1]):
        if character == "1":
            actions_list.append(actions.get(index))

    is_reverse = (actions_list != []) and (actions_list[-1] == "reverse")
    if is_reverse:
        actions_list.pop(-1)
        actions_list.reverse()
    
    return actions_list
    
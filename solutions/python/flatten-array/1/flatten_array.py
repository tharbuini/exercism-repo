def flatten(iterable):
    flatten_list = []

    for item in iterable:
        if type(item) == type(int()):
            flatten_list.append(item)
        
        if type(item) == type(list()):
            sub_list = flatten(item)
            for sub_item in sub_list:
                if type(sub_item) == type(int()):
                    flatten_list.append(sub_item)
                    
    return flatten_list
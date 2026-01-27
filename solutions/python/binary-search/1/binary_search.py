def find(search_list, value):
    search_list.sort()
    
    first_index = 0
    last_index = len(search_list)
    control = last_index
    middle = ((last_index - first_index) // 2)
    
    while control > 0:
        if last_index == 1 and search_list[0] == value:
            return 0
        
        if search_list[middle] == value:
            return middle
        elif search_list[middle] < value:
            first_index = middle
            middle += ((last_index - first_index) // 2)
        else:
            last_index = middle
            middle -= ((last_index - first_index) // 2)
        
        control -= 1

    raise ValueError("value not in array")
    
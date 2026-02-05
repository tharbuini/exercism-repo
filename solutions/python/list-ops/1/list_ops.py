def append(list1, list2):
    for item in list2:
        list1.append(item)
    
    return list1
    
def concat(lists):
    flattened_list = []
    for list_ in lists:
        for item in list_:
            flattened_list.append(item)

    return flattened_list

def filter(function, list):
    true_items = []
    for item in list:
        if function(item) == True:
            true_items.append(item)
    
    return true_items

def length(list):
    return len(list)

def map(function, list):
    items = []
    for item in list:
        items.append(function(item))

    return items

def foldl(function, list, initial):
    accumulator = initial

    for item in list:
        accumulator = function(accumulator, item)

    return accumulator

def foldr(function, list, initial):
    accumulator = initial

    for item in list[::-1]:
        accumulator = function(accumulator, item)

    return accumulator

def reverse(list):
    return list[::-1]

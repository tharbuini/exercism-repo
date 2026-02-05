def sum_of_multiples(limit, multiples):

    multiples_list = set()
    for item in multiples:
        for number in range(limit):
            if (item * number) >= limit:
                break
            multiples_list.add(item * number)

    sum = 0
    for item in multiples_list:
        sum += item
    
    return sum

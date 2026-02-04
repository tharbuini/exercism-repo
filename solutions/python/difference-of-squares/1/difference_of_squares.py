def square_of_sum(number):
    result = 0
    for n in range(number + 1):
        result += n

    return result ** 2

def sum_of_squares(number):
    result = 0
    for n in range(number + 1):
        result += n ** 2

    return result

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

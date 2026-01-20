def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    i = 1
    aliquot_sum = 0
    while i < number:
        if number % i == 0:
            aliquot_sum += i
        i += 1

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"

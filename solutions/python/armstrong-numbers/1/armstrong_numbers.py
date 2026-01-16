def is_armstrong_number(number):
    if number == 0:
        return True

    string_number = str(number)
    length = len(string_number)
    if length == 1:
        return True
        
    sum = 0
    for index in range(length):
        sum += int(string_number[index]) ** length

    if sum == number:
        return True
    else:
        return False

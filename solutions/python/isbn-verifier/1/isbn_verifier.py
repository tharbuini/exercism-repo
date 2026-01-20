def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False

    i = 10
    result = 0
    for digit in isbn:
        if digit == "X" and i == 1:
            digit = "10"
        
        if digit.isalpha():
            return False
        
        result += int(digit) * i
        i -= 1
    
    if result % 11 == 0:
        return True
    else:
        return False

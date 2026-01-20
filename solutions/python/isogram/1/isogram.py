def is_isogram(string):
    chars = []
    string = string.lower()
    string = string.strip()
    
    for char in string:
        chars.append(char)
        string = string.replace(char, "", 1)
        if char in string and char.isalpha():
            return False

    return True

def rotate(text, key):
    if key == 0:
        return text
    
    cipher_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.isalpha():
            position_alphabet = alphabet.index(char.lower())
            new_char = alphabet[(position_alphabet + key) % 26]
            if char.isupper():
                new_char = new_char.upper()
            cipher_text += new_char
        else:
            cipher_text += char
    
    return cipher_text

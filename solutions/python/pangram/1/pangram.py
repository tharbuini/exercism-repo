def is_pangram(sentence):

    if len(sentence) < 26:
        return False
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
                
    for char in sentence.lower():
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
            
    if alphabet != "":
        return False
    else:
        return True

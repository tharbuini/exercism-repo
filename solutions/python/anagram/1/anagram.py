def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
            
        treated_word = word.lower()
        extra_chars = []
            
        for char in candidate.lower():
            if char in treated_word:
                treated_word = treated_word.replace(char, "", 1)
            else:
                extra_chars.append(char)
        
        if not treated_word and not extra_chars:
            anagrams.append(candidate)

    return anagrams
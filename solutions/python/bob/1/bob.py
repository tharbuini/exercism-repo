def response(hey_bob):
    try:
        is_question = hey_bob.rstrip()[-1] == "?"
    except:
        is_question = False
    is_yelling = hey_bob.isupper()
    is_silence = hey_bob.strip() == ""
    if is_yelling:
        if is_question:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"  
    if is_question:
        return "Sure."
    if is_silence: 
        return "Fine. Be that way!"
    else:
       return "Whatever." 

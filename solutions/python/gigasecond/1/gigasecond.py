import datetime

def add(moment):
    gigasecond = 1000000000
    duration = datetime.timedelta(seconds=gigasecond)
    
    new_date = moment + duration
    return new_date

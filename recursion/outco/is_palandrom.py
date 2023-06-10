def first_char(string):
    return string[0]

def last_char(string):
    return string[-1]

def middle_char(string):
    return string[1:-1]

def is_palinedrome(string):
    if len(string) in {0, 1}:
        return True
    if first_char(string) != last_char(string):
        return False
    return is_palinedrome(middle_char(string))

def check_palandrom(string):
    print(f"the word {string} is : ", is_palinedrome(string))


check_palandrom("racecar")
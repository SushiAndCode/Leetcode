
def removeStars(s: str) -> str:
    i = 0
    while "*" in s:

        if s[i] == "*":
            s = s[:i-1] + s[i+1:]
            i = 0
        i += 1
    
    return s


removeStars("leet**cod*e")
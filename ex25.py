def isSubsequence(s: str, t: str) -> bool:
    mini = -1
    count = 0
    if not s:
        return True
    for j,c in enumerate(s):
        if c not in t:
            return False
        for i,ca in enumerate(t):
            if c == ca and i > mini:
                mini = i
                count+=1
                break
        
        if count == len(s):
            return True

    if count < len(s):
            return False

isSubsequence("aza","abzba")
def reverseVowels(s: str) -> str:
    s = list(s)
    i = 0
    j = len(s)-1
    vocali = ["a","e","i","o","u","A","E","I","O","U"]

    while i < (len(s)-1)/2:
        if s[i] in vocali:
            while s[j] not in vocali:
                j -=1
            appo = s[j]
            s[j] = s[i]
            s[i] = appo
            j -=1
        i +=1
    return ''.join(s)

reverseVowels("IceCreAm")
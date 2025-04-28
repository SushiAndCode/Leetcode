def gcdOfStrings(str1: str, str2: str) -> str:
    index = 0
    answer = ""
    check = set()
    
    while str1[index] == str2[index]:

        if str2[index] not in check:
            answer = answer + str2[index]  
            check.add(str2[index])
        else:
            return answer
        
        index += 1
        
    return ""

gcdOfStrings("ABCABC", "ABC")
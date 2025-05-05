def maxVowels(s: str, k: int) -> int:
        i = 0
        vow = ["a","e","i","o","u"]
        count = 0
        mas = 0
        fir = s[i:i+k]
        while i+k < len(s):
            if i == 0 :
                for let in fir:
                    if let in vow:
                        count += 1
            elif i != 0:
                if s[i+k-1] in vow:
                    count += 1
                if s[i-1] in vow:
                    count -= 1
            if count == k:
                return count
            if count > mas:
                mas = count
            i += 1
        return mas

maxVowels("abciiidef",3)
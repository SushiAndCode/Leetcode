def decodeString( s: str) -> str:
        stringa = ""
        cip = 0
        i = 0
        num = ""
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        while i < len(s):
            if s[i] == "]":
                j = i
                while j > 0:
                    
                    if s[j] == "[":
                        n = j-1
                        while s[n] in nums:
                            num = s[n] + num
                            cip += 1
                            n -= 1
                        val = int(num)
                        num = ""
                        stringa = val*s[j+1:i]
                        s = s[0:j-cip] + stringa + s[i+1:]
                        i = i + len(stringa) - (i-j+cip) - 1
                        cip = 0
                        break
                    else:
                        j -= 1
            else:
                i += 1
        
        return s


decodeString("3[a12[c]]")

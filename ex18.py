def mergeAlternately(word1: str, word2: str) -> str:
        stringa = ""
        index1 = 0
        index2 = 0
        
        for i in range(len(word1) + len(word2)):
            if i % 2 == 0:
                stringa = stringa + word1[index1]
                index1 += 1
            elif i % 2 == 1:
                stringa = stringa + word2[index2]
                index2 += 1

            if index2 >= len(word1):
                stringa = stringa + word2[index2:]
            
            if index1 > len(word2):
                stringa = stringa + word1[index1:]

            if len(stringa) == (len(word1) + len(word2)):
                print(stringa)
                return stringa
            
        print(stringa)
        return stringa

mergeAlternately("apbr","aq")
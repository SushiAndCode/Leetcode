def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
             return []
        
        numbers = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        if len(digits) == 1:
             return list(numbers[digits])
        ans = []
        k = 1
        prima = [x for x in numbers[digits[0]]]
        while k < len(digits):
            for digit in numbers[digits[k]]:
                supp = list(map(lambda x: x+digit,prima))
                ans = ans + supp
                supp = []
            prima = ans
            ans = []
            k+=1 
        return prima

print(letterCombinations("2"))
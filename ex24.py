def increasingTriplet(self, nums: list[int]) -> bool:
    first = second = float('inf') 
    for n in nums: 
        if n <= first: 
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
        

increasingTriplet([1,5,0,4,1,3])
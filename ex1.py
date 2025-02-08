def summs(nums, target):
    for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if x+y == target and i != j:
                    return [i,j]
            

print(summs([3,3],6))
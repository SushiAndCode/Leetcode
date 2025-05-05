def pivotIndex(nums: list[int]) -> int:
        
    for i in range(len(nums)):

        if i == 0 and sum(nums) == 0:
            return 0
        elif sum(nums[i+1:]) == sum(nums[0:i]):
            return i
        
    return -1

pivotIndex([1,7,3,6,5,6])
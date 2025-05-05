def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
    ans1 = set()
    ans2 = set()

    for i in nums1:
        if i not in nums2:
            ans1.add(i)

    for i in nums2:
        if i not in nums1:
            ans2.add(i)
    
    return list[list(ans1),list(ans2)]

findDifference([1,2,3], [2,4,6])
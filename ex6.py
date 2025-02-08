from itertools import combinations
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if sum(nums) == 0 and len(nums)%3 == 0:
        return list(zip(*[iter(nums)]*3))
    finalList = set()
    duets = set()
    appo = []
    j = 0
    for i,n in enumerate(nums):
        appo.append(nums[i])
        while sum(appo) != 0 or len(appo) < 3:
            if i != j:
                appo.append(nums[j])
                if tuple(sorted(appo)) not in duets:
                    if sum(appo) == 0 and len(appo) == 3 and tuple(sorted(appo)) not in finalList:
                        finalList.add(tuple(sorted(appo)))
                        break
                    if (sum(appo) != 0 and len(appo) == 3) or tuple(sorted(appo)) in finalList:
                        appo.pop()
                else:
                    appo.pop()
            j+=1           
            if j >= len(nums):
                break        
        if len(appo) == 2:
            duets.add(tuple(sorted(appo))) 
        else:
            for pair in combinations(tuple(sorted(appo)), 2):
                duets.add((pair))
        j = 0
        appo=[]
    return list(finalList)

threeSum([3,0,-2,-1,1,2])
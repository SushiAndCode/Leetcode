import numpy as np
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    height = np.array(height)
    if not len(height):
        return 0
    maxx = 0
    area = 0
    
    for i,n in enumerate(height):
        for greater in np.where(n <= height)[0]:
            if greater != i:
                area = n*abs(greater-i)
            if area > maxx:
                maxx = area
    return maxx

maxArea([1,8,6,2,5,4,8,3,7])
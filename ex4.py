def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxx = 0
    area = 0
    for i,a in enumerate(height):
        for j,b in enumerate(height):
            if i!=j:
                area = abs(j-i)*min(a,b)
            if area > maxx:
                maxx = area
    return maxx   
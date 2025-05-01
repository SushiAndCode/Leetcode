def maxArea(height: list[int]) -> int:
    maxx = 0
    for i,h in enumerate(height):
        j = i+1
        while j < len(height):
            if (min(height[j],h) * (j-i)) > maxx:
                maxx = (min(height[j],h) * (j-i))
            j+=1

    return maxx

print(maxArea([1,8,6,2,5,4,8,3,7]))
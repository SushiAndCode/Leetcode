from collections import Counter

def equalPairs(grid: list[list[int]]) -> int:

    counter = 0

    rows = [x for x in grid]
    columns = [list(x) for x in zip(*grid)]

    for i in rows:
        for j in columns:
            if i == j:
                counter += 1
    
    return counter


print(equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))


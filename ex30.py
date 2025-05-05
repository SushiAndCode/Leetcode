def uniqueOccurrences(arr: list[int]) -> bool:
        arr.sort()
        arr.sort()
        counter = 1
        counters = []
        for i in range(len(arr)):
            if i+1 < len(arr):
                if arr[i] == arr[i+1]:
                    counter += 1
                elif counter in counters:
                    return False
                else:
                    counters.append(counter)
                    counter = 1
            elif i == len(arr)-1:
                if counter in counters:
                    return False

        return True

uniqueOccurrences([1,2])
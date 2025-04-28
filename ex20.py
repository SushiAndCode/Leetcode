def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        
        index = 0
        m = 0

        for i in range(len(flowerbed)):

            if index < len(flowerbed):
                if flowerbed[index] == 0 and flowerbed[index] == flowerbed[index+1]:
                    index += 2
                    m += 1
                else:
                    index += 1
            if index >= len(flowerbed):
                break
        
        if m >= n:
            return True
        else:
            return False


canPlaceFlowers([1,0,0,0,0,0,1], 2)
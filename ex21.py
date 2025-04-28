

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        
        index = 0
        m = 0

        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[0] == 0 and flowerbed[1] == 0: 
                    flowerbed[0] = 1
                    m += 1
                    continue

            if i == len(flowerbed)-1:     
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    m += 1
                    continue

            if i-1 >= 0 and i+1 <= len(flowerbed):
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    m += 1

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            m += 1
        
        if m >= n:
            return True
        else:
            return False 

print(canPlaceFlowers([1,0,0,0,1,0,0],2))
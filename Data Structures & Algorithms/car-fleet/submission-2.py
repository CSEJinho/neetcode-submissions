class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nArr = [(p, s) for p, s in zip(position, speed)]
        nArr.sort(reverse=True)
        fleets = 1
        prevTime = (target - nArr[0][0]) / nArr[0][1]        

        for i in range(1, len(nArr)):
            currCar = nArr[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
            
                

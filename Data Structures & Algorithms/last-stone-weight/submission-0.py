import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = []

        for stone in stones:
            heapq.heappush(result, stone * -1)
        
        while len(result) > 1:
            x = heapq.heappop(result) * -1
            y = heapq.heappop(result) * -1
            if x == y:
                continue
            else:
                z = (x - y) * -1
                heapq.heappush(result, z)
        
        if not result:
            return 0
        else:
            return result[0] * -1


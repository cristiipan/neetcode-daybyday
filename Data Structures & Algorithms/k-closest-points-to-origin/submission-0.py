import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(result, (-dist, point))
            if len(result) > k:
                heapq.heappop(result)
        
        return [point for _, point in result]

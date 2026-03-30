import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []

        for num in nums:
            heapq.heappush(result, num)
            if len(result) > k:
                heapq.heappop(result)

        return result[0]        
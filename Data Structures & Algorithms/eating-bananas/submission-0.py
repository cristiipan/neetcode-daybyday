class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, h, k):
            hours_needed = 0

            for pile in piles:
                hours_needed += (pile + k - 1) // k
            
            if hours_needed <= h:
                return True
            else:
                return False

        k1 = 1
        k2 = max(piles)

        while k1 < k2:
            mid = (k1 + k2) // 2
            if canFinish(piles, h, mid):
                k2 = mid
            else:
                k1 = mid + 1
        
        return k1
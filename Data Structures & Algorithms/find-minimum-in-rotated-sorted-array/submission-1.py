class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
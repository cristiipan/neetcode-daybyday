class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_map:
                return [prev_map[complement], i]
            prev_map[num] = i

        return []
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints = defaultdict(int)

        for i, num in enumerate(nums):
            complement = target - num
            if complement in ints:
                return [ints[complement], i]
            ints[num] = i
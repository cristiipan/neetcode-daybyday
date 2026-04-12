class Solution:
    def backtrack(self, nums, target, total, startIndex, path, result):
        if total > target:
            return
        
        if total == target:
            result.append(path[:])
            return
        
        for i in range(startIndex, len(nums)):
            total += nums[i]
            path.append(nums[i])
            self.backtrack(nums, target, total, i, path, result)
            path.pop()
            total -= nums[i]

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(nums, target, 0, 0, [], result)
        return result
        
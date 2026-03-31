class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reviewed = set()
        for num in nums:
            if num not in reviewed:
                reviewed.add(num)
            else:
                return True
        return False

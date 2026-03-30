"""
哈希表需要额外开辟一块随输入大小增长的空间，是 O(n)；
双指针只用两个变量，是 O(1)。
这道题要求 O(1) 空间，所以必须用双指针而不是哈希表。

时间：O(n)，最多遍历一次
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]

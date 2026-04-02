class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)     # we put all the numbers in a set to eliminate all duplicates
        longest = 0             # the final result to return

        for num in num_set:     # we iterate through the whole set (instead of the list)
            if num - 1 not in num_set:
                # if num-1 is not in the set
                # then it's possible that num could be the beginning of a consecutive sequence
                # this avoids reprocessing the same sequence multiple times
                # ensuring overall O(n) time complexity
                # if it's only num itself, then the length would be just 1
                length = 1
                while num + length in num_set:
                    # we keep checking if the next, the next, the next... num is in the set
                    # to do so we keep extending the length
                    length += 1
                
                longest = max(longest, length)
        
        return longest
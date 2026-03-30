"""
strategy here:
we start by putting 2 pointers, one at the beginning of the heights list and the other at the end
this can guarantee that this container has the longest width
at this point, if we want to find a different container
this means the width will narrow down
the only chance that this container can be 'bigger'
is when the height is higher
so we should move the lower pointer, in order to find a higher pointer
cause the height is determined by the lower points of the two
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1

        while i < j :
            max_area = max(max_area, min(heights[i], heights[j]) * (j - i))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
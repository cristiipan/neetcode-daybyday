"""
Strategy:
We use a sliding window to find the longest substring that can be made 
into a single repeating character with at most k replacements.

Eligibility condition:
A window is valid if: window_length <= max_freq + k
where max_freq is the frequency of the most frequent character in the window.

Implementation:
As we move the right pointer, we:
1. Update a hashmap to track the frequency of each character in the window
2. Update max_freq = max(max_freq, char_map[s[right]])

Key insight: max_freq only ever increases — when the window shrinks,
we do NOT update max_freq downward. This is safe because a smaller 
max_freq would only produce a shorter window, which can never beat 
our recorded max_length.

If the window becomes invalid (window_length > max_freq + k):
1. Decrement the frequency of s[left] in the hashmap
2. Move left pointer right by one

After each valid window, update max_length = max(max_length, right - left + 1)
------ UMPIRE ------
[Understand]
- We can replace AT MOST k characters in a window
- Goal: find the longest substring where all chars are the same after replacements
- Edge case: empty string → return 0 (covered by general logic)

[Match]
- Sliding window: window validity depends on its content → classic pattern
- Hashmap: need to track character frequencies within window

[Plan]
- Validity condition: window_length <= max_freq + k
- max_freq only increases — safe to skip downward updates when shrinking window
- Move left pointer when window becomes invalid

[Evaluate]
- Time: O(n) — single pass
- Space: O(1) — hashmap bounded by character set size (26 uppercase letters)
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if len(s) == 1:  no need for this edge case it's already covered in subsequent logics
        #     return 1
        
        left = 0
        max_freq = 0
        char_map = defaultdict(int)
        max_length = 0      # max_length 记录的是历史上出现过的最长**合法**窗口，而不是当前窗口的大小。
                            # 所以整个算法的逻辑是：
                            # 窗口扩大时 → 检查是否合法 → 如果合法，尝试更新 max_length
                            # 窗口缩小时 → 只是为了维持"不比历史最大更差"的状态 → 不需要更新 max_length

        for right in range(len(s)):
            char_map[s[right]] += 1
            max_freq = max(max_freq, char_map[s[right]])

            while right - left + 1 > max_freq + k:
                char_map[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
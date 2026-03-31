"""
in order for a permutation of s1 become a substring of s2
all character exists in s1 should appear in s2 with same frequency and all the ones don't exist shouldn't appear
so the length of this substring of s2 should = length of s1
this makes me think of sliding window, and the length of this window is set, it's the same length as s1
when we find a window in s2, that matches all the frequency of characters in s1, this is our window

how to implement:
we use a hashmap to track all the frequency of distinct characters in s1
we create a window in s2, that matches the length of s1
we iterate this window, each character we pass by, if it already exist in s1, its value in the map -1
we use a "matches" to track all the matched character
when a value in the map becomes "0", then "matches" + 1
when we reach till the end of this window, and "matches" != len(map), we move this window to the right
we remove the left character, if the value was 0 before this, then "matches"-1, its value in map + 1
we add the right character, its value in map - 1, if the value becomes 0, matches + 1
⬆️ 注意左右character加入之后，matches +- 1 和value -+ 1的顺序是相反的
when we reach the end of s2, if "matches" == len(map), return true
else return false

❌ 如果 s2 里出现了 s1 没有的字母：
用 defaultdict(int)，char_map["z"] 初始为 0，-1 之后变成 -1。
这个字符的 value 永远不会变成 0（除非后来被 +1 抵消），所以不会触发 matches += 1，也就不会影响合法判断。自然被忽略了 ✅
⬆️ 这个思路的核心错误分析：
1. len(char_dict) 是动态变化的
你使用了 defaultdict(int)。在 Python 中，当你访问一个不存在于字典中的键时（例如 char_dict[s2[right]]），defaultdict 会自动为这个键创建一个条目，默认值为 0。
后果：即使 s2 中的字符不在 s1 中，只要你访问了它，它就会进入 char_dict。
影响：你的判断条件 if matches == len(char_dict) 会因为 len(char_dict) 的不断增加而永远无法成立。

2. matches 的统计逻辑存在歧义
你的逻辑是“当某个字符的计数变为 0 时，matches += 1”。
如果 s2 中出现了一个不在 s1 中的字符（比如 'x'），你执行 char_dict['x'] -= 1，它的值变成了 -1。
当这个 'x' 从窗口左侧移出时，你执行 char_dict['x'] += 1，它的值从 -1 变回了 0。
此时你的代码触发了 if char_dict[s2[left]] == 0: matches -= 1（在移出前判断），这会导致 matches 的数值出现逻辑混乱，因为它统计了本不该关心的字符。
"""
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        char_dict = Counter(s1)
        required = len(char_dict)
        
        n = len(s1)
        left = 0
        matches = 0

        for right in range(len(s2)):
            char_r = s2[right]
            if char_r in char_dict:
                char_dict[char_r] -= 1
                if char_dict[char_r] == 0:
                    matches += 1

            if right >= n:
                char_l = s2[left]
                if char_l in char_dict:
                    if char_dict[s2[left]] == 0:
                        matches -= 1
                    char_dict[char_l] += 1
                left += 1
        
            if matches == required:
                return True

        return False

"""
关键点总结
固定目标：不要用 len(char_dict) 作为动态判断标准，要在循环开始前用一个变量（如 required）记录 s1 中有多少种不同的字符。
条件过滤：在处理 s2 的字符时，先用 if char in char_dict 判断。这样字典里就只会有 s1 里的字符，不会被 s2 里的杂质字符污染。
窗口时机：滑动窗口的本质是“一进一出”。先处理 right 移入，如果窗口超长，再处理 left 移出。
"""
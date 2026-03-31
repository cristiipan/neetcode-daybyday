from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        chars = defaultdict(int)

        for i in range(n):
            chars[s[i]] += 1

        for i in range(n):
            chars[t[i]] -= 1
        
        for value in chars.values():
            if value != 0:
                return False

        return True
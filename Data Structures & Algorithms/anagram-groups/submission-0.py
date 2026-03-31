class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagram_groups = {}

        for s in strs:
            sorted_key = ''.join(sorted(s))
            if sorted_key not in anagram_groups:
                anagram_groups[sorted_key] = []
            
            anagram_groups[sorted_key].append(s)
        
        return list(anagram_groups.values())
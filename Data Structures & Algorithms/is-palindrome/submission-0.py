class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:  # 空字符串/全非法字符视为回文
            return False
        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1

        """
        三个 while i < j 各司其职：外层控制整体循环，两个内层分别帮左右指针跳过非法字符；
        内层也必须带 i < j 条件，防止跳过非法字符时两个指针互相越过对方导致越界
        """
        while i < j:  # as long as i is to the left of j, we continue compare
            while i < j and not s[i].isalnum():
                i += 1  # make sure we find a isalnum item that is to the right of j (cause i can continue to grow)
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
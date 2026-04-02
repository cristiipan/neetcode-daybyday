class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = ""
        # for s in strs:
        #     res += str(len(s)) + "#" + s
        # return res

        # 两种写法逻辑完全等价，下面这种写法在字符串很多的时候性能更好
        # 因为 += 每次都会创建新字符串对象，而 list + join 只在最后拼接一次
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
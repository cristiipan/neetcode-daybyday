class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, open, close):
            if open == n and close == n:
                res.append(path)

            if open < n:
                # path + "("  如果这么写的话，就生成了新字符串，但没有保存，也没有传进递归
                # open += 1
                backtrack(path + "(", open + 1, close)
            if close < open:
                # path + ")"
                # close += 1
                backtrack(path + ")", open, close + 1)

        backtrack("", 0, 0)
        return res
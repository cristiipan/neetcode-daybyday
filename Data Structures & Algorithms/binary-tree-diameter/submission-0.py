# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]       # 用 list 存 res，因为 Python 内层函数不能直接修改外层的不可变变量。res = 0 是一个整数，整数是不可变类型（immutable）。内层 dfs 想修改它必须声明 nonlocal，否则 Python 会把 res 当作局部变量处理。用 list 绕过了这个问题，因为 list 是可变类型（mutable），内层函数可以直接修改它的内容，不需要重新赋值。

        def dfs(root):
            if not root:
                return -1       # 这里空树设置为-1更方便计算（因为single node tree高度为0）
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res[0]
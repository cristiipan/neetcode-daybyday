# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        self.vec.append(root.val)
        self.traversal(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec = []
        self.traversal(root)
        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i - 1]:
                return False
        return True
        
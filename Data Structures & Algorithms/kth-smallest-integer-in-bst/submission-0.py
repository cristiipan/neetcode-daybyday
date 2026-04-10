# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, node):
        if node is None:
            return
        self.traversal(node.left)
        self.vec.append(node.val)
        self.traversal(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vec = []
        self.traversal(root)
        return self.vec[k - 1]
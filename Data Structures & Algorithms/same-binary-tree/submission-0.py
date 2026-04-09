# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        return self.compare(p, q)
    
    def compare(self, a, b) -> bool:
        if a == None and b == None:
            return True
        if a == None and b != None:
            return False
        if a != None and b == None:
            return False
        
        if a.val != b.val:
            return False
        
        left = self.compare(a.left, b.left)
        right = self.compare(a.right, b.right)
        isSame = left and right

        return isSame
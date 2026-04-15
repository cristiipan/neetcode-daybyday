"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}       # a hashmap to track all the nodes we have visited / copied

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]       # if we have already made a copy of this node, we don't need to make another copy we just return the copy

            copy = Node(node.val)           # if it's not copied already, we make a copy
            oldToNew[node] = copy           # we add it to the hashmap, map the old node to the new copy
            for nei in node.neighbors:      # for all the neighbors that the original node has, we run dfs on it
                copy.neighbors.append(dfs(nei))        # it's going to return a new copy of the node neighbor, and we just append them to the new copy node as its new neighbors
            return copy

        return dfs(node)
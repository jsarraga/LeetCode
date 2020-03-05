
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
                
        def isMirror(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isMirror(l.left, r.right) and isMirror(l.right, r.left)
            return False
        
        if root is None:
            return False
        
        return isMirror(root.left, root.right)
        
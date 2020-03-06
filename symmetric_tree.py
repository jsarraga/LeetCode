#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
                
        # make a function that checks if left anf right are mirrors
        def isMirror(l, r):
            # if both are None - they are a mirror --> True
            if not l and not r:
                return True
            # if l and r AND they both are the same value
            if l and r and l.val == r.val:
                # we'll check outer pairs bottom left leaf(l.left [3 in example]) and bottom right leaf (r.right or 3[3 in example])
                # AND we'll check the inner pairs (l.right [4 in example]) and (r.left [4 in example])
                return isMirror(l.left, r.right) and isMirror(l.right, r.left)
            # if none of that checks out, return false
            return False
        
        if root is None:
            return False
        
        return isMirror(root.left, root.right)
        
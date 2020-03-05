

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        # checks if the two trees are the same
        def sameTree(p, q):
            if p and q:
                return p.val == q.val and sameTree(p.left, q) and sameTree(p.right, q)
            return p is q
        
        # if s is None, there can be no subtree --> false
        if s is None:
            return False
        # checks if the trees are the same --> True
        if sameTree(s, t):
            return True
        # checks left subtree and right subtree to see if there is a match to t
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        else:
            return False
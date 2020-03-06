# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        output = []
        p = self.preorder(p, output)
        q = self.preorder(q, output)
        return p == q
        
    #  traverse the tree in preorder (root, left, right) --> check that solution if need explanation
    #  then compare the two
    def preorder(self, root, output):
        output = []
        self.helper(root, output)
        return output
        
    def helper(self, root, output):
        if not root:
            output.append("None")
        else:
            output.append(root.val)
            self.helper(root.left, output)
            self.helper(root.right, output)
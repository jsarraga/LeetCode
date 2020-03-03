#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9  

# invert to

#     4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            # if there's a root. swap left and right.
            # swaps to recursion invert to go down to another level of the tree
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
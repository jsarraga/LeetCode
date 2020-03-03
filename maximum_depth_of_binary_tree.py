#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # goes down one level, adds 1, then recusively does that for each node (adds 1 for every iteration of recursion)
        # then takes the max depth of both sides
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
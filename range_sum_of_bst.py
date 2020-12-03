# A Binary Search Tree (BST) is has the following attributed:
# - The left subtree of a node contains only nodes with keys lesser than the node’s key.
# - The right subtree of a node contains only nodes with keys greater than the node’s key.
# - The left and right subtree each must also be a binary search tree. 
# - There must be no duplicate nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# APPROACH: pre-order traversal of binary tree
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # must use a list so it doesn't get overwritten with every pass
        output = [0]
        def helper(root, output):
            if root:
                if root.val >= low and root.val <= high:
                    output[0] += root.val
                # recursively run it on the left and right
                helper(root.left, output)
                helper(root.right, output)
        helper(root, output)
        return output[0]
        
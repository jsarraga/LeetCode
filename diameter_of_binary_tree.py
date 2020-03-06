# similar to max depth, except you use a counter 
# the diameter is the length between two nodes - meaning, how many levels between 4,5 and 3.
# the path would be 4->2, 2->1, 1->3 == 3

    #       1
    #      / \
    #     2   3
    #    / \     
    #   4   5 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.result = 0
    
        def depth(root):
            if not root:
                return 0
            else:
                left = depth(root.left)
                right = depth(root.right)
                # diameter is the longest possible path between the left and right sub-trees 
                # (hence adding the depth of left + right) 
                # (ie, the path from the bottom-most leaf in the left tree to the bottom-most leaf in the right tree === left + right).
                self.result = max(self.result, left + right)
                # returns 1 (counts the root) + the longest of the left and right legs
                return 1 + max(left, right)

        depth(root)
        return self.result

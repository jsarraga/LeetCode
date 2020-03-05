# input:
#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        output = []

        # make a helper function to traverse the tree
        # adding each node plus "->" to a string at every level
        # append the string to a list after iteration

        def path(root, string, output):
            # add the string value to string
            string += str(root.val)

            if root.left:
                # by passing in '->' as string arg it becomes: (existing) string + '->' += root.val
                # and adds the '->' before adding the str(root.val)
                path(root.left, string + '->', output)
            if root.right:
                path(root.right, string + '->', output)
                # if it's the last leaf, we'll append the string to output
            if not root.left and not root.right:
                output.append(string)

        # handles for an empty tree
        if not root:
            return []
        
        # initiate the string to an empty one so we can add to it
        path(root, '', output)
        return output






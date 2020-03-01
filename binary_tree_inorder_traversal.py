# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# inorder traveral = left, root right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        self.helper(root, output)
        
        return output
        
            
    def helper(self, root, output):
        if not root:
            pass
        else:
            # checks left side first. If null, pass
            self.helper(root.left, output)
            # else: appned root.val
            output.append(root.val)
            # check right side after 
            self.helper(root.right, output)
    
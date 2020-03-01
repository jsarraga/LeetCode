# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# SAME SOLUTION AS INORDER TRAVERSAL, BUT A DIFFERENT ORDER
# preorder traversal: root, left, right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.helper(root, output)
        return output
    
        
    def helper(self, root, output):
        if not root:
            pass
        else:
            output.append(root.val)
            self.helper(root.left, output)
            self.helper(root.right, output)
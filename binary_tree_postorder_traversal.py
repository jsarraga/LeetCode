# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# SAME SOLUTION AS BINARY TREE INORDER TRAVERSAL, PREORDER TRAVERSAL, BUT A DIFFERENT ORDER
# postorder traversal: left, right, root

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.helper(root, output)
        return output


    def helper(self, root, output):
        if not root:
            pass
        else:
            self.helper(root.left, output)
            self.helper(root.right, output)
            output.append(root.val)
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
        lleft = self.preorderTraversal(root.left)
        lright = self.preorderTraversal(root.right)
        return [root.val] + lleft + lright
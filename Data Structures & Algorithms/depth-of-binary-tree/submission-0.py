# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(root):
            if root==None:
                return 0

            if root.left==None and root.right==None:
                return 1
            elif root.left==None and root.right:
                return 1+depth(root.right)
            elif root.left and root.right==None:
                return 1 + depth(root.left)
            else:
                return max(1+depth(root.left),1+depth(root.right))

        return depth(root)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def depth(root):
            if root ==None:
                return 0,0
            
            left_height,left_diameter=(depth(root.left))
            right_height,right_diameter=(depth(root.right))
            height=1+max(left_height,right_height)
            through_root=left_height+right_height
            diameter = max(left_diameter,right_diameter,through_root)
            return height, diameter

        return depth(root)[1]
        

        

            


                

            
        
        
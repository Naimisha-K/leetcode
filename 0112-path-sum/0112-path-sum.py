# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag=False
        def traverse(node,sum):
            nonlocal flag
            if not node or flag:
                return 
            sum+=node.val
            if not node.left and not node.right:
                if sum==targetSum:
                    flag=True
                return
            traverse(node.left,sum)
            traverse(node.right,sum)
        traverse(root,0)
        return flag
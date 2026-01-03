# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum=[0]
        def getleftLeavesSum(node,isLeft):
            if not node:return
            if not node.left and not node.right and isLeft:
                sum[0]+=node.val
                return
            getleftLeavesSum(node.left,True)
            getleftLeavesSum(node.right,False)
        getleftLeavesSum(root,False)
        return sum[0]
            

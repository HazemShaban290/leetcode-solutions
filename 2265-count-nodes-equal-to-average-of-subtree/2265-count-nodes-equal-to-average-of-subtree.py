# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res=[0]
        def countNode(node):
            if not node: return 0 ,0
            leftSum,leftcount=countNode(node.left)
            rightSum,rightcount=countNode(node.right)
            totalSum=leftSum+rightSum+node.val
            totalCount=leftcount+rightcount+1
            avr=totalSum//totalCount
   
            if avr == node.val:
                res[0]+=1
            return totalSum,totalCount
        countNode(root)
        return res[0]
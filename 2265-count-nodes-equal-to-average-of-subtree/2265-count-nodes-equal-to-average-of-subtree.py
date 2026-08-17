# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=[0]

        def getAvrNodesCount(node):
            if node is None:
                return 0,0
            leftSum,leftCount=getAvrNodesCount(node.left)
            rightSum,rightCount=getAvrNodesCount(node.right)
            avr=(node.val+leftSum+rightSum)//(leftCount+rightCount+1)
            if avr==node.val:
                count[0]+=1
            return node.val+leftSum+rightSum,leftCount+rightCount+1
        getAvrNodesCount(root)
        return count[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def getAvrNodesCount(node):
            if node is None:
                return 0,0,0
            leftSum,leftCount,leftMatches=getAvrNodesCount(node.left)
            rightSum,rightCount,rightMatches=getAvrNodesCount(node.right)
            avr=(node.val+leftSum+rightSum)//(leftCount+rightCount+1)
            matches=rightMatches+leftMatches
            if avr==node.val:
                matches+=1
            return node.val+leftSum+rightSum,leftCount+rightCount+1,matches
        getAvrNodesCount(root)
        return getAvrNodesCount(root)[2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes=[]
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            nodes.append(node)
            inOrder(node.right)
        inOrder(root)
        currSum=0
        for i in range(len(nodes)-1,-1,-1):
            currSum+=nodes[i].val
            nodes[i].val=currSum
        return root
            
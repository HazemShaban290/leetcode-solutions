# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        mostLeftNode=[root.val,0]
        def getLeftMost(node,depth):
 
            if not node.left:
                if depth>mostLeftNode[1]:
                    mostLeftNode[0]=node.val
                    mostLeftNode[1]=depth
            if node.left:
                getLeftMost(node.left,depth+1)
            if node.right:
                getLeftMost(node.right,depth+1)
        getLeftMost(root,0)
        return mostLeftNode[0]
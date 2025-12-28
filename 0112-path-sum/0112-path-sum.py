# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        q=deque()
        q.append((root,root.val))
        while q :
            node,currSum=q.popleft()
            if node.left :
                q.append((node.left,currSum+node.left.val))
            if node.right :
                q.append((node.right,currSum+node.right.val))
            if not node.right and not node.left:
                if currSum == targetSum:
                    return True
        return False
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=deque()
        q.append((root,1))
        while q :
            node,level=q.popleft()
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
            
            if not q or q[0][1]>level:
                node.next=None
            else:
                node.next=q[0][0]
        return root
        
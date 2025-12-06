"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        oldToNewHashMap={}
        node=head
        while node:
            oldToNewHashMap[node]=Node(node.val)
            node=node.next
        node=head
        while node:
            oldToNewHashMap[node].next=oldToNewHashMap.get(node.next)
            oldToNewHashMap[node].random=oldToNewHashMap.get(node.random)
            node=node.next
        return oldToNewHashMap[head]
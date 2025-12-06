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
        index=1
        newHead=Node(head.val)
        node2=newHead
        node1=head
        hashMapOne={head:index}
        hashMapTwo={index:newHead}
        while  node1:
            index+=1
            node1=node1.next
            if not node1:break
            hashMapOne[node1]=index
            newNode=Node(node1.val)
            node2.next=newNode
            node2=node2.next
            hashMapTwo[index]=node2
            
        node1=head
        node2=newHead
        while node1:
            if node1.random:
                node2.random = hashMapTwo[hashMapOne[node1.random]]
            node1=node1.next
            node2=node2.next
        return newHead
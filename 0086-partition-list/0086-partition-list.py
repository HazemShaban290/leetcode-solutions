# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(float('-inf'),head)
        lastSmallerNode=dummy
        node=head
        prev=dummy

        while node:

            if node.val<x:
                if node == lastSmallerNode.next:
                    lastSmallerNode=lastSmallerNode.next
                    node=node.next
                    prev=prev.next
                else:
                    next=lastSmallerNode.next
                    lastSmallerNode.next=node
                    prev.next=node.next
                    node.next=next
                    lastSmallerNode=lastSmallerNode.next
                    node=prev.next
            else:
                node=node.next
                prev=prev.next
        return dummy.next
        
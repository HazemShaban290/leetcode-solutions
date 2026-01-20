# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(n1,n2):
            while n1%n2!=0:
                tamp = n2
                n2=n1%n2
                n1=tamp
            return n2
        node=head
        while node and node.next:
            newNode=ListNode(GCD(max(node.val,node.next.val),min(node.val,node.next.val)))
            
            next=node.next
            node.next=newNode
            newNode.next=next
            node=next
        return head
    
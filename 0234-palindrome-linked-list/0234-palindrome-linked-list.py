# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        prev,next=None,None
        curr=node
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        node1=self.reverse(slow)
        node2=head
        while node1 and node2:
            if node1.val==node2.val:
                node1=node1.next
                node2=node2.next
            else:
                return False
        return True
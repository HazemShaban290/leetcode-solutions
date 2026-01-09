# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        def getLength(node):
            length=0
            while node:
                length+=1
                node=node.next
            return length
        length=getLength(head)
        k=k%length
        if k==0:
            return head
        first=head
        last=head
        print(length,first,last,k)
        for _ in range(k):
            last=last.next
        while last.next:
            first=first.next
            last=last.next
        newHead=first.next
        first.next=None
        last.next=head
        return newHead
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1,list1)
        prev=dummy
        curr=list1
        curr2=list2
        while curr and curr2 :
            if curr.val<=curr2.val:
                curr=curr.next
                prev=prev.next
            else:
                prev.next=curr2
                next2=curr2.next
                curr2.next=curr
                prev=curr2
                curr2=next2
        if curr2:
            prev.next=curr2
        return dummy.next
                

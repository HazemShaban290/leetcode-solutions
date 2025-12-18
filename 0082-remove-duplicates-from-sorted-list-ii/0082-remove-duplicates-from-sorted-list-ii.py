# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head :return head
        dummy =ListNode(None,head)
        prev=dummy
        curr = head
        while curr and curr.next:
            if curr.next and curr.val==curr.next.val:
                duplicate=curr.val
                while curr and curr.val == duplicate:
                    curr=curr.next
                prev.next=curr
            else:
                curr=curr.next
                prev=prev.next
        return dummy.next
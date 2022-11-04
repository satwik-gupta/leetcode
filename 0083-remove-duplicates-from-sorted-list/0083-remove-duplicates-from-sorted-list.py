# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        while(c):
            while(c.next and c.val==c.next.val):
                c.next=c.next.next
            c=c.next
        return head
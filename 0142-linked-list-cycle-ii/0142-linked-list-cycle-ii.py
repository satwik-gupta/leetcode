# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #floyd warshall algorithm
        a,b,c=head,head,head
        iscycle=0
        while(a and a.next):
            b=b.next
            a=a.next.next
            
            if(a==b):
                iscycle= 1
                break
        if(iscycle==0):
            return None
        while(b!=c):
            c=c.next
            b=b.next
        return b
                
        
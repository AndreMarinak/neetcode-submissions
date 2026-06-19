# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        p1=head
        p2=head
        prev=None
        temp=0
        while temp<n: #1,2 N=2, so remove 1
            p2=p2.next
            temp+=1
        while p2!=None:
            prev=p1
            p2=p2.next
            p1=p1.next
        if prev==None:
            return p1.next
        else:
            prev.next=p1.next
            return head

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        dummy=ListNode()

        head=dummy       
        if lists==[]:
            return None
        for lst in lists:
            if lst==None:
                continue
            else:
                curr=lst
                while curr:
                    heapq.heappush(h,curr.val)
                    curr=curr.next
        while len(h) > 0:
            dummy.next= ListNode(heapq.heappop(h))
            dummy=dummy.next
        dummy.next=None
        return head.next

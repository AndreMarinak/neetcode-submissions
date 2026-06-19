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
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(h, (lst.val, i, lst))


        while len(h) > 0:
            val, i, node = heapq.heappop(h)
            dummy.next = node
            dummy = dummy.next
            
            # 5. THE OPTIMIZATION: Now add the next node from that specific list
            if dummy.next:
                heapq.heappush(h, (node.next.val, i, node.next))
                
        dummy.next = None
        return head.next
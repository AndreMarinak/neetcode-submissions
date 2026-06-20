import heapq
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # 1. Initialize heaps (using negative values for max-heap behavior in Python)
        left_heap = []
        right_heap = []
        
        # Populate the right heap with ALL elements initially
        # We store (-height, index) so we know when an item is outdated
        for i, h in enumerate(height):
            heapq.heappush(right_heap, (-h, i))
            
        total_water = 0
        
        # 2. Iterate through the array
        for i, current_height in enumerate(height):
            
            # Add current block to left heap
            heapq.heappush(left_heap, -current_height)
            
            # Remove current block (and any previous ones) from right heap
            # We only care if the absolute max on the right is behind us
            while right_heap and right_heap[0][1] <= i:
                heapq.heappop(right_heap)
                
            # Get max left (guaranteed to exist since we just pushed to it)
            max_left = -left_heap[0]
            
            # Get max right (if heap is empty, there is no right boundary)
            max_right = -right_heap[0][0] if right_heap else 0
            
            # Calculate water
            # We use max(0, ...) because if the current block is the tallest
            # on the right, min(max_left, max_right) - current_height would be negative.
            water_at_index = max(0, min(max_left, max_right) - current_height)
            
            total_water += water_at_index
            
        return total_water
import heapq
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_left=[]
        max_right=[]
        temp_max=0
        for i in range(len(height)):
            new_max=(max(height[i],temp_max))
            max_left.append(new_max)
            temp_max=new_max
        temp_max=0
        for num in reversed(height):
            new_max=(max(num,temp_max))
            max_right.append(new_max)
            temp_max=new_max
        max_right.reverse()
        total=0


        for i in range(len(height)):
            total+= ( min(max_left[i],max_right[i]) - height[i] )
        return total




class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area=0

        #while l<r:
        while r-l>=1:
            if min((heights[l],heights[r])) * (r-l) > max_area:
                max_area= min((heights[l],heights[r]))*(r-l)

            move=min(heights[l],heights[r])
            if move==heights[l]:
                l+=1
            else:
                r-=1

        return max_area

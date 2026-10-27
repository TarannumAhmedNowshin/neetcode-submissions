class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxx_area=0
        left =0
        right= len(heights)-1
        while left<right:
  
            w=right-left
            h=min(heights[left],heights[right])
            area=w*h
            maxx_area=max(area,maxx_area)
            if heights[left]< heights[right]:
                left+=1
            else:
                right-=1
        return maxx_area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i,j=0,len(height)-1
        while i<j:
            if height[j]>height[i]:
                area=height[i]*(j-i)
                i+=1
                
            else:
                area=height[j]*(j-i)
                j-=1
            max_area=max(max_area,area)
        return max_area

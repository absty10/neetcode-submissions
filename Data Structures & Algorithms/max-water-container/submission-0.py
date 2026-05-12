class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                length=min(heights[i],heights[j])
                breadth=j-i
                currArea=length * breadth
            
                if currArea>area:
                    area=currArea
        
        return area
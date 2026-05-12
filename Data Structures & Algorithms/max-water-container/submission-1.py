class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        length=len(heights)
        i=0
        j=length-1
        while(i<j):
            l=min(heights[i],heights[j])
            b=j-i
            currArea=l*b
            print(i,j,currArea)
            if currArea>area:
                area=currArea
            print(area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return area
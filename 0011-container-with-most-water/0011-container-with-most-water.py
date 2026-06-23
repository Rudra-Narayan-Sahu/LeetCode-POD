class Solution(object):
    def maxArea(self, height):
        maxarea=0
        left=0
        right=len(height)-1
        while left<=right:
            w=right-left
            h=min(height[left],height[right])
            area=w*h
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
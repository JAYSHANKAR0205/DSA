class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        i=0
        j=len(height)-1
        while i<j:
            width=j-i
            ht=min(height[i],height[j])
            area=width*ht
            max_water=max(max_water,area)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water

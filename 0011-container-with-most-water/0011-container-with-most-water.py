class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # inv_height = height[::-1]
        # for i in range(len(height)):
        #     for j in range(len(height[:-i-1])):
        #         area = min(height[i], inv_height[j]) * (len(height) - i - j - 1)
        #         max_area = max(max_area, area)
        #         if inv_height[j] > height[i]:
        #             break
        # return max_area
        l, r = 0, len(height) - 1
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return max_area
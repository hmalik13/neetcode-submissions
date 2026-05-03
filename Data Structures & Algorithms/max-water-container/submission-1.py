class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointers
        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            h = min(heights[l], heights[r])
            water = (r - l) * h
            maxWater = max(water, maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater





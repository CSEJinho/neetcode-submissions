class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l, r = 0, length - 1
        maxsize = 0
        while l < r:
            cursize = min(heights[l], heights[r]) * (r - l)
            maxsize = max(cursize, maxsize)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxsize




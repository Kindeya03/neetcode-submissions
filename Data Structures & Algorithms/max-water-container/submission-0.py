class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f = 0
        r = len(heights)-1
        maxA = 0
        while f < r:
            a = min(heights[f], heights[r])* (r-f)
            maxA = max(maxA, a)
            if heights[f] <= heights[r]:
                f +=1
            else:
                r -=1
        return maxA
        
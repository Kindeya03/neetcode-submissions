class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = float("-inf")
        if len(prices)<=1:
            return 0
        lower = float("inf")
        for i in range(1, len(prices)):
            lower = min(prices[i-1], lower)
            maxprof = max(maxprof, prices[i]-lower)
        return max(maxprof, 0)
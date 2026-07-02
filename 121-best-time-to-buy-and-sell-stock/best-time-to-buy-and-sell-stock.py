class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=float("inf")
        for i in prices:
            mini=min(mini,i)
            maxi=max(maxi,i-mini)
        return maxi
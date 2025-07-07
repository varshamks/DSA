class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mip=float('inf')
        mp=0
        for price in prices:
            mip=min(mip,price)
            mp=max(mp,price-mip)
        return mp
        
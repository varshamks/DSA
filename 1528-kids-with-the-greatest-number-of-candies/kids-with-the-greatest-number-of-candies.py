class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc=max(candies)
        return [extraCandies+c>=mc for c in candies]
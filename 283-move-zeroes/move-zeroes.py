class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in nums:
            if i!=0:
                nums[c]=i
                c=c+1
        while c<len(nums):
            nums[c]=0
            c=c+1

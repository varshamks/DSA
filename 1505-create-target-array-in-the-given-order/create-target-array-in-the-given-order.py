class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        r=[]
        for i,idx in enumerate(index):
            r.insert(idx,nums[i])
        return r
        
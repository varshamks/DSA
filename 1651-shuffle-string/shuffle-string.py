class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r=['']*len(s)
        for i,indx in enumerate(indices):
            r[indx]=s[i]
        return ''.join(r)

        
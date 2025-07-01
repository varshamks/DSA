class Solution:
    def toLowerCase(self, s: str) -> str:
        r=''
        for i in s:
            if 'A'<= i <='Z':
                r+=chr(ord(i)+32)
            else:
                r+=i
        return r
        
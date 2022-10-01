class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s[0] == '0':
            return 0
        a=1
        b=1
        for i in range(1,len(s)):
            if(s[i] != '0'):
                c=a
            else:
                c=0
            if (s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6'):
                c+= b
            b=a
            a=c
        return a
            
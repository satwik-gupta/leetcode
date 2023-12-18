class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        if(n<5):
            return 0
        else:
            while(n>=5):
                n//=5
                c+=n
            return c
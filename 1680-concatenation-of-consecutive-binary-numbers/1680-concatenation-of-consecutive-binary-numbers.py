class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def binaryToDecimal(n):
            return int(n,2)
        binary=''
        mod=10**9 + 7
        for i in range(1,n+1):
            binary+=bin(i).replace('0b','')
        decimal=binaryToDecimal(binary)
        
        return decimal%mod
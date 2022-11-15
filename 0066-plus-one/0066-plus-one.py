class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        num=0
        for i in range(len(digits)):
            num+=digits[i]*(10**i)
        res=[]
        num=num+1
        while(num>0):
            n=num%10
            num=num//10
            res.append(n)
        return res[::-1]
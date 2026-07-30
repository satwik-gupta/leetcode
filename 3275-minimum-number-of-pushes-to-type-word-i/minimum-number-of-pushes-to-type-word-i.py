class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        count=0
        for i in range(0,n):
            mul=math.ceil((i+1)/8)
            count+=1*mul
        return count
    

        

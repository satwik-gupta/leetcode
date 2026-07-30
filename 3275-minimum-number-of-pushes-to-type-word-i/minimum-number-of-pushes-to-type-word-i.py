class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        count=8
        for i in range(8,n):
            mul=math.ceil((i+1)/8)
            count+=1*mul
        return count
    

        

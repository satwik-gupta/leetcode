class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if(low%2==0 and high%2!=0 or low%2!=0 and high%2==0 or low%2==0 and high%2==0):
            return (high - low + 1)//2
        elif(low%2!=0 and high%2!=0 ):
            return (high - low + 1)//2 + 1
            
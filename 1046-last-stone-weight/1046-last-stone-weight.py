class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones)>1):
            stones.sort()
            m1=stones[-1]
            m2=stones[-2]
            if(m1==m2):
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones.pop(-1)
                stones.pop(-1)
                stones.append(m1-m2)
        if(len(stones)>0):
            return stones[0]
        else:return 0
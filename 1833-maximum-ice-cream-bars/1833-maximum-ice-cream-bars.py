class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n=0
        spent=0
        for i in range(len(costs)):
            if((spent+costs[i])<=coins):
                n+=1
                spent+=costs[i]
            else:
                break
        return n
            
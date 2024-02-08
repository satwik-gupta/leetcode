class Solution:
    def numSquares(self, n: int) -> int:
        sq = {j ** 2 for j in range(1, 101) if j ** 2 <= n}
        
        if n in sq:
            return 1
        
        sq2 = {x+y for x in sq for y in sq if x+y <= n}
        
        if n in sq2:
            return 2
        
        sq3 = {x+y for x in sq2 for y in sq if x+y <= n}
        
        if n in sq3:
            return 3
        
        return 4
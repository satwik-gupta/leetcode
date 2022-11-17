from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = set(Counter(deck).values())
        gcd_val = next(iter(count))
        for c in count:
            gcd_val = gcd(gcd_val, c)
            if gcd_val == 1: return False
        return True
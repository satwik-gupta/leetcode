class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        commas=n-1000 +1
        return commas
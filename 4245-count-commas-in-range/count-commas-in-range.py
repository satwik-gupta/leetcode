class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        commas=n-999
        return commas
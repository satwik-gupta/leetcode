class Solution:
    def strStr(self, hs: str, needle: str) -> int:
        n = len(hs)
        m = len(needle)
        if m == 0:
            return 0
        lsd = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = lsd[j - 1]
            if needle[j] == needle[i]:
                j += 1
            lsd[i] = j
        j = 0
        for i in range(n):
            while j > 0 and needle[j] != hs[i]:
                j = lsd[j - 1]
            if needle[j] == hs[i]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
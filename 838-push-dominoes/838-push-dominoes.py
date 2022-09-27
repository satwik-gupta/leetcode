class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = list(dominoes)
        l, n = 0, len(dominoes)
        for r in range(n):
            if d[r] == '.':
                continue
            elif (d[r] == d[l]) or (d[l] == '.' and d[r] == 'L'):
                for k in range(l, r):
                    d[k] = d[r]
            elif d[l] == 'L' and d[r] == 'R':
                pass
            elif d[l] == 'R' and d[r] == 'L':
                m = (r - l - 1) // 2
                for k in range(1, m + 1):
                    d[r - k] = 'L'
                    d[l + k] = 'R'
            l = r
        if d[l] == 'R':
            for k in range(l, n):
                d[k] = 'R'
                
        return ''.join(d)
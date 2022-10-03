class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        row = ([1] * k + [0] * (target - k))[:target]

        mod = 10**9 + 7
        for i in range(n - 1):
            # start updating row from the end
            row[target - 1] = sum(row[max(0, target - 1 - k): target - 1]) % mod
            for t in range(target - 2, max(-1, target - 1 - (n - 1 - i) * k), -1):
                row[t] = (row[t + 1] - row[t] + (row[t - k] if t - k >= 0 else 0)) % mod

        return row[-1]
        
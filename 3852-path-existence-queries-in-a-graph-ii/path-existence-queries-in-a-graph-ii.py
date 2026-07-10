from typing import List

class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        # 1. Faster sorting using C-level __getitem__ instead of a lambda
        idx = sorted(range(n), key=nums.__getitem__)
        
        # 2. Populate pos array
        pos = [0] * n
        for i, v in enumerate(idx):
            pos[v] = i

        m = n.bit_length()
        
        # 3. Build the first layer (j = 0) of our sparse table
        f0 = [0] * n
        left = 0
        for i in range(n):
            while left < i and nums[idx[i]] - nums[idx[left]] > maxDiff:
                left += 1
            f0[i] = left

        # 4. Transposed binary lifting table: f[j][i] instead of f[i][j]
        # This enables list comprehensions which run at C-speed in Python.
        f = [f0]
        for _ in range(1, m):
            prev = f[-1]
            f.append([prev[p] for p in prev])

        res = []
        # 5. Direct tuple unpacking in loops to avoid repeated indexing
        for u, v in queries:
            x, y = pos[u], pos[v]
            
            if x > y:
                x, y = y, x

            if x == y:
                res.append(0)
                continue

            step = 0
            # 6. Binary lifting step
            for i in range(m - 1, -1, -1):
                if f[i][y] > x:
                    y = f[i][y]
                    step += 1 << i

            if f[0][y] <= x:
                res.append(step + 1)
            else:
                res.append(-1)

        return res
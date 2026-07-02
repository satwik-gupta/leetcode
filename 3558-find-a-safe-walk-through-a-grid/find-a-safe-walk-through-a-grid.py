from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        # Health remaining after entering the starting cell
        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        # best[r][c] = maximum health remaining seen so far
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health

        q = deque([(0, 0)])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            current_health = best[r][c]

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                new_health = current_health - grid[nr][nc]

                if new_health <= 0:
                    continue

                if new_health > best[nr][nc]:
                    best[nr][nc] = new_health
                    q.append((nr, nc))

        return False
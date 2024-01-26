class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Define a recursive function with memoization using @cache decorator
        @cache
        def recursive_run(i, j, moves):
            # Base case: if out of grid boundaries, return 1 (a path is found)
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            # Base case: if no moves remaining, return 0 (no valid path)
            elif moves == 0:
                return 0
            
            # Explore four possible moves and accumulate the results
            ans = recursive_run(i + 1, j, moves - 1)
            ans += recursive_run(i - 1, j, moves - 1)
            ans += recursive_run(i, j + 1, moves - 1)
            ans += recursive_run(i, j - 1, moves - 1)
            
            return ans

        # Call the recursive function with the initial position and maxMove,
        # and return the result modulo (10**9 + 7)
        return recursive_run(startRow, startColumn, maxMove) % (10**9 + 7)
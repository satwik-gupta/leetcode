class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        import math

        res = [[0, 0]]
        heights_heap = [(0, math.inf)]
        # heights_heap[0] - is the smallest element

        events = [(left, -height, right) for left, right, height in buildings]
        events += list(set([(right, 0, 0) for _, right, _ in buildings]))
        events.sort()

        for pos, height, right in events:
            # if curr pos >= positions in heap
            while heights_heap[0][1] <= pos:
                heapq.heappop(heights_heap)
            if height != 0:
                heapq.heappush(heights_heap, (height, right))
            if res[-1][1] != -heights_heap[0][0]:
                res += [[pos, -heights_heap[0][0]]]

        return res[1:]
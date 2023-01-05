class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        LastHit = -(2**32)
        n = 0
        for i in points:
            if i[0] > LastHit:
                n += 1
                LastHit = i[1]
        return n
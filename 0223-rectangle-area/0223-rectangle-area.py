class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        area2 = abs(bx1 - bx2) * abs(by1 - by2)
        
        if (bx1 < ax2 and ax1 < bx2) and (by1 < ay2 and ay1 < by2):
            rx1 = max(ax1, bx1)
            rx2 = min(ax2, bx2)
            ry1 = max(ay1, by1)
            ry2 = min(ay2, by2)
            return area1 + area2 - abs(rx1 - rx2) * abs(ry1 - ry2)
        
        return area1 + area2
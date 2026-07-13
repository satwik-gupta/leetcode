from typing import List

class Solution:
    # 1. Precompute all 36 sequential numbers at the class level
    ALL_NUMS = []
    for i in range(1, 9):
        num = i
        for j in range(i + 1, 10):
            num = num * 10 + j
            ALL_NUMS.append(num)
            
    # 2. Sort them once
    ALL_NUMS.sort()

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 3. List comprehension running at C-speed to filter the answers
        return [x for x in self.ALL_NUMS if low <= x <= high]
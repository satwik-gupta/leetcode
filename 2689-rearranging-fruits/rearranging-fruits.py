class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total_freq = freq1 + freq2

        # Check if total frequencies are all even
        for v in total_freq.values():
            if v % 2 != 0:
                return -1

        # Minimum value of any fruit
        min_val = min(min(basket1), min(basket2))

        # Calculate surplus in each basket
        diff = []
        for k in total_freq:
            d = freq1[k] - total_freq[k] // 2
            diff.extend([k] * abs(d))

        # Only need to fix half of the surplus
        diff.sort()
        n = len(diff) // 2

        cost = 0
        for i in range(n):
            cost += min(diff[i], 2 * min_val)

        return cost
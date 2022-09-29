class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        n = len(arr)
        l, r = idx-1, idx
        while r-l < k+1:
            if l < 0:
                r = k
            elif r > n-1:
                l = n-k-1
            else:
                rd, ld = abs(arr[r] - x), abs(arr[l] - x)
                if rd < ld:
                    r += 1
                else:
                    l -= 1
        return arr[l+1:r]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]*(rowIndex+1);
        n = rowIndex
        r = 1
        for i in range(1, n):
            ans[i] = ans[i-1]*n//r;
            n = n - 1
            r = r + 1
        return ans;
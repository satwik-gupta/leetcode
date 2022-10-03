class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        def cal(tmp):
            res = 0
            x = tmp
            while x != 0:
                r = x % 10
                x = x // 10
                res += r*r
            return res
        while n != 1:
            n = cal(n)
            if n in hashMap.keys():
                return False
            hashMap[n] = 1
        return True
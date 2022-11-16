# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        if n==1:
            return 1
        while left <= right:
            mid = (left + right) // 2
            if guess(mid)==-1:
                right = mid
            elif(guess(mid)==0):
                return mid
            else:
                left = mid + 1
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# [1, 3, 5, 7]
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            mid = (l + r) // 2
            if guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
            else:
                return mid

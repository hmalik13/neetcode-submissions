class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left = 0
        top = 0
        right = n
        bottom = n

        cur = 1
        while cur <= (n*n):
            # populate top row
            for i in range(left, right):
                res[top][i] = cur
                cur += 1
            top += 1
            # populate right column
            for i in range(top, bottom):
                res[i][right - 1] = cur
                cur += 1
            right -= 1
            # populate bottom row
            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = cur
                cur += 1
            bottom -= 1
            # populate left column
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = cur
                cur += 1
            left += 1
        return res

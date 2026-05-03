class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom:
            midrow = (top + bottom) // 2
            if target > matrix[midrow][right]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bottom = midrow - 1
            else:
                row = midrow
                break
        
        if not (top <= bottom):
            return False

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[midrow][mid]:
                left = mid + 1
            elif target < matrix[midrow][mid]:
                right = mid - 1
            else:
                return True
        return False




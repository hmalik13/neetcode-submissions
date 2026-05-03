class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1

        # process each layer of matrix
        while left < right:
            # rotate each element in current layer
            for i in range(right - left):
                top = left
                bottom = right
                # save top left
                topLeft = matrix[top][left + i]
                # bottom left -> top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # bottom right -> bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # top right -> bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # top left -> top right
                matrix[top + i][right] = topLeft
            # update pointers
            left += 1
            right -= 1







        

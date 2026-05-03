class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top = l
                bottom = r
                # save topLeft
                topLeft = matrix[top][l + i]
                # put bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # put bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # put top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # put top left into top right
                matrix[top + i][r] = topLeft
            # once we've rotated outer square, we have to move inward
            l += 1
            r -= 1
            


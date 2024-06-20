class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row, col = len(matrix), len(matrix[0]) - 1

        while top <= bottom:
            mid = (bottom + top) // 2
            if target > matrix[mid][col]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        left, right = 0, len(matrix[mid]) - 1
        row = mid
        while left <= right:
            mid = (right + left) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False

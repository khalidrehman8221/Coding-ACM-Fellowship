class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid // n][mid % n]

            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

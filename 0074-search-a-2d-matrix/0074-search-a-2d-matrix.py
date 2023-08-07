class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1
        
        
        while top <= bottom:
            mid = (top + bottom)//2
            print(top, bottom, mid)
            if target in matrix[mid]:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        
        return False
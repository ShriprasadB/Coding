class Solution:
    def generate(self, numRows: int):
        
        arr = [[1],[1,1]]
        
        if numRows == 1:
            return [arr[0]]
        if numRows == 2:
            return arr
        
        for i in range(3, numRows + 1):
            level = [1]
            for j in range(1, len(arr[-1])):
                level.append(arr[-1][j - 1] + arr[-1][j])
            level.append(1)
            arr.append(level)
        
        return arr
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for c in range(0,n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
            
        for r in range(0,m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
        
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    
        return dp[-1][-1]
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0]*(m + 1) for i in range(n + 1)]

        for i in range(1, m+1):
            dp[0][i] = ord(s2[i - 1]) + dp[0][i-1]
        
        for i in range(1, n+1):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]
        

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1])
        
        return dp[-1][-1]
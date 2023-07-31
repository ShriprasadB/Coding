class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1, s2 = s, s[::-1]
        n = len(s)
        dp = [[0]*(n+1) for i in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[-1][-1]

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for i in range(n)]

        def solve(l, r):
            if dp[l][r] != -1:
                return dp[l][r]
            
            dp[l][r] = n
            j = -1

            for i in range(l, r):
                if s[i] != s[r] and j == -1:
                    j = i
                if j != -1:
                    dp[l][r] = min(dp[l][r], 1 + solve(j, i) + solve(i + 1, r))
            
            if j == -1:
                dp[l][r] = 0
            
            return dp[l][r]

        return 1 + solve(0, n-1)
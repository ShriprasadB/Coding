class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4000:
            return 1

        dp = [[-1]*(n + 1) for i in range(n+1)]
        operations = [(100, 0), (75, 25), (50, 50), (25, 75)]

        def probability(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            
            if A <= 0:
                return 1
            
            if B <= 0:
                return 0

            if dp[A][B] != -1:
                return dp[A][B]
            
            p = 0
            for a_serve, b_serve in operations:
                p += 0.25*probability(A - a_serve, B - b_serve)
            
            dp[A][B] = p
            return p

        return probability(n, n)


        
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = collections.defaultdict(int)

        for s in strs:
            mCnt, nCnt = s.count("0"), s.count("1")
            for M in range(m, mCnt - 1, -1):
                for N in range(n, nCnt - 1, -1):
                    dp[(M, N)] = max(dp[M, N], 1 + dp[(M - mCnt, N - nCnt)])

        return dp[(m, n)]
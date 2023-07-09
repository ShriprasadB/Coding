class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        sum_ = sum_//2
        n = len(nums)

        """
        Brute force + memoization
        @lru_cache(maxsize = None)
        def dfs(i, nums, sum_):
            if sum_ == 0:
                return True
            
            if i == 0 or sum_ < 0:
                return False
            
            result = dfs(i - 1, nums, sum_) or dfs(i - 1, nums, sum_ - nums[i - 1])
            return result

        return dfs(n - 1, tuple(nums), sum_)        
        
        #dynamic programming
        dp = [[False] * (sum_ + 1) for i in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            cur = nums[i - 1]
            for j in range(sum_ + 1):
                if j < cur:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - cur]
        
        return dp[n][sum_]
        """


        dp = set()
        dp.add(0)
        
        for i in range(n - 1, -1, -1):
            nextdp = dp.copy()
            for j in dp:
                nextdp.add(nums[i] + j)
            dp = nextdp
        
        return sum_ in dp
                
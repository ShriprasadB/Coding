class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        dp = [[-1]*(2*total + 1) for i in range(n)]
        
        def dfs(i, sum_):
            if i == len(nums):
                if sum_ == target:
                    return 1
                return 0

            if dp[i][total + sum_] != -1:
                return dp[i][total + sum_]

            dp[i][total + sum_] = dfs(i + 1, sum_ + nums[i]) + dfs(i + 1, sum_ - nums[i])
            return dp[i][total + sum_]
    
        return dfs(0, 0) 
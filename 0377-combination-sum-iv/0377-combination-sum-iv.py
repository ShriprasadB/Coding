
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
    
        dp = defaultdict(lambda: 0)
        dp[0] = 0
        
        for i in range(1,target+1):
            if i in nums:
                dp[i] = 1+ sum([dp[i-num] for num in nums])
            else:
                dp[i] = sum([dp[i-num] for num in nums])

        return dp[target]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        sum_ = sum_/2
        n = len(nums)

        @lru_cache(maxsize = None)
        def dfs(i, nums, sum_):
            if sum_ == 0:
                return True
            
            if i == 0 or sum_ < 0:
                return False
            
            result = dfs(i - 1, nums, sum_) or dfs(i - 1, nums, sum_ - nums[i - 1])
            return result

        return dfs(n - 1, tuple(nums), sum_)
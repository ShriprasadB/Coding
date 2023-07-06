class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        min_len = float('inf')
        sum_ = 0

        for i in range(n):
            sum_ += nums[i]
            while sum_ >= target:
                min_len = min(min_len, i - start + 1)
                sum_ -= nums[start]
                start += 1

        return min_len if min_len != float('inf') else 0
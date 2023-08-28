class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] < k:
                max_sum = max(max_sum, nums[l] + nums[r])
                l += 1
            else:
                r -= 1
        
        return max_sum
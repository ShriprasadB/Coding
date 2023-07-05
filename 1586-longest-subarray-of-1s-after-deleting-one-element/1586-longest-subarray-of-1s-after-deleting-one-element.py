class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        start = 0
        max_len = 0
        i = 0

        while start < n and i < n:
            if nums[i] == 0:
                count += 1
                if count == 1:
                    next_start = i + 1
            
                if count == 2:
                    max_len = max(max_len, i - start - count)
                    count = 0
                    start = next_start
                    i = next_start
                    continue

            max_len = max(max_len, i - start + 1 - count)
            i += 1
        
        return max_len - 1 if max_len == n else max_len
            

            

            

            
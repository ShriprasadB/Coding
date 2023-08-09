class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r, res = 0, nums[-1] - nums[0], float("inf")
        
        def isValid(m):
            i, count = 0, 0

            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= m:
                    count += 1
                    i += 2
                else:
                    i += 1

            return count >= p

        while l <= r:
            m = (l + r)//2

            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res


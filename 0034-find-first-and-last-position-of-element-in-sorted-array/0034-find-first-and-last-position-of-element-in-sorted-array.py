class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if target == nums[m]:
                l, r = m, m
                while l - 1 >= 0 and nums[l - 1] == nums[l]:
                    l -= 1
                while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                    r += 1

                return [l, r]

            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return [-1, -1]
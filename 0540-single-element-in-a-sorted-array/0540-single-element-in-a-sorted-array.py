class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = (i + j)//2
            if nums.count(nums[mid]) == 1:
                return nums[mid]
            elif nums.count(nums[i]) == 1:
                return nums[i]
            elif nums.count(nums[j]) == 1:
                return nums[j]
            else:
                i += 2
                j -= 2
        
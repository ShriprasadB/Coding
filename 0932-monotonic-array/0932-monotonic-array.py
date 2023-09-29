class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        c = 1
        for i in range(0,len(nums)-1):   
            if nums[i] <= nums[i+1]:
                c = c + 1
                
        if c == len(nums):
            return True
        
        d = 1
        for i in range(0,len(nums)-1):
            if nums[i] >= nums[i+1]:
                d = d + 1
                
        if d == len(nums):
            return True
            
            
        return False
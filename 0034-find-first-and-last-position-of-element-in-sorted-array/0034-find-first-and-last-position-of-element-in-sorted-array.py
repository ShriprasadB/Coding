class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] == target:
                low, high = mid, mid
                while 0 < low and nums[low] == nums[low - 1]:
                    low -= 1
                
                while high < len(nums) - 1 and nums[high] == nums[high + 1]:
                    high += 1
                
                return [low, high]
                
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return [-1, -1]
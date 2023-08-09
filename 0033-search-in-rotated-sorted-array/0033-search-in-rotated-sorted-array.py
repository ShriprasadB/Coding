class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target < nums[left]:
                    left = mid + 1
                elif target < nums[mid] and target >= nums[left]:
                    right = mid - 1

            elif nums[left] > nums[mid]:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target > nums[right]:
                    right = mid - 1
                elif target > nums[mid] and target <= nums[right]:
                    left = mid + 1

        return -1
        
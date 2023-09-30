class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = len(nums)

        if k < 3:
            return False

        min_array = [-1] * k
        min_array[0] = nums[0]
        for i in range(1, k):
            min_array[i] = min(min_array[i - 1], nums[i])

        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while k < len(nums) and nums[k] <= min_array[j]:
                k += 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False
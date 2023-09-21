class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i, num in enumerate(nums):
            if num in dict1:
                return [dict1[num], i]
            else:
                dict1[target - num] = i

        
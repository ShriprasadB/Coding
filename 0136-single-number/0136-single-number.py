class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            #x-or operation 
            result = result ^ n

        return result
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        xor &= -xor

        result1, result2 = 0, 0

        for n in nums:
            if xor & n == 0:
                result1 ^= n
            else:
                result2 ^= n
        
        return [result1, result2]
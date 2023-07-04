class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n, answer, p = len(nums), 0, 0

        for i in range(32):
            total_bits = 0
            for j in range(n):
                total_bits += (nums[j] >> i) & 1
            
            total_bits = total_bits % 3
            answer += total_bits*(2**p)
            p += 1

        return answer if (-2**31 <= answer <= 2**31 - 1) else answer - (2**32)  
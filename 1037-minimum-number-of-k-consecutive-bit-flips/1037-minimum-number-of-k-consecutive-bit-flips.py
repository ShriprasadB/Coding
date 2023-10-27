class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        f = [0] * len(nums)
        psum = 0
        for i in range(len(nums)-k+1):
            if (psum + nums[i])%2 == 0:
                f[i] = 1
            psum += f[i]
            if i-k+1 >= 0:
                psum -= f[i-k+1]
        for i in range(len(nums)-k+1, len(nums)):
            if (psum+nums[i])%2 == 0:
                return -1
            if i-k+1 >= 0:
                psum -= f[i-k+1]  
        return sum(f)
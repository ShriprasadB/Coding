class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            
            parts = nums[i]//nums[i + 1]

            if nums[i] % nums[i + 1]:
                parts += 1
            
            answer += parts - 1

            nums[i] = nums[i]//parts

        return answer
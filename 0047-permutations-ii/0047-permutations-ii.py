class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = collections.defaultdict(int)
        answer = []
        perm = []

        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                answer.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop(-1)

        dfs()
        return answer
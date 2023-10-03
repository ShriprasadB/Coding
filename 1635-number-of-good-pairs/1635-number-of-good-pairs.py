class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        result = 0
        for num in nums:
            dict1[num] += 1
        
        for k, v in dict1.items():
            result += comb(v, 2)

        return result
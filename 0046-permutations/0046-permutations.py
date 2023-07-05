class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]

        for n in nums:
            temp = []
            for perm in result:
                for j in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(j, n)
                    temp.append(perm_copy)

            result = temp

        return result

            
        
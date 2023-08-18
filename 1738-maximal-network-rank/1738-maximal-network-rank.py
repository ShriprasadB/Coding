class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        
        dict1 = collections.defaultdict(list)
            
        for n1, n2 in roads:
            dict1[n1].append(n2)
            dict1[n2].append(n1)
        
        max_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                sum_ = len(dict1[i]) + len(dict1[j])
                if i in dict1[j]:
                    sum_ -= 1
                max_rank = max(max_rank, sum_)
                
                
        return max_rank
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sum_ = {}
        for i in range(len(mat)):    
            sum_[i] = sum(mat[i])
            
        a = [i for i, j in sorted(sum_.items(), key=lambda item: item[1])]
        
        return a[:k]
            
        
        
        
        
        
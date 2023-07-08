class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = [0]* (n - 1)
        min_, max_ = 0, 0
        
        for i in range(1, n):
            pairs[i - 1] = weights[i] + weights[i - 1]
        
        pairs.sort()

        for i in range(k - 1):
            min_ += pairs[i]
            max_ += pairs[n - i - 2]

        return max_ - min_


        

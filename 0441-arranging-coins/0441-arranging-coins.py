class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = (l + r)//2
            sum_ = (m*(m + 1))//2
            if sum_ == n:
                return m

            if  sum_ < n:
                l = m + 1
            
            else:
                r = m - 1
        
        return r
            
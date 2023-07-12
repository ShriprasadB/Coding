class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n>0:
            if n == 1:
                return True
            while n > 1:
                if n%2 == 0:
                    n = n/2
                    if n == 1:
                        return True
                    
                else:
                    return False
                
            
        else:
            return False
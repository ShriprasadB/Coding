class Solution:
    def fib(self, n: int) -> int:
        one = 0
        two = 1
        
        if n == 0:
            return one
        if n == 1:
            return two
        
        for i in range(2, n + 1):
            temp = two
            two = one + two
            one = temp
            
        return two
        
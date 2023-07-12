class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            if n == 1:
                return True
            else:
                while n > 1:
                    if n % 3 == 0:
                        n = n//3
                        if n == 1:
                            return True

                    else:
                        return False

        else:
            return False
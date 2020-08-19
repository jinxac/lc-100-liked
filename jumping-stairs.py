class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n == 3:
            return 3
        
        i = 3
        a = 2
        b = 3
        c = 3
        
        while i < n:
            c = a + b 
            a = b
            b = c
            i += 1
        
        return c

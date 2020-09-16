class Solution:
    
    def backtrack_with_constraint(self, n):
        res = []
        def bt_with_constraints(s = "", o = 0, c = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if o < n:
                bt_with_constraints(s + "(", o + 1, c)
            
            if c < o:
                bt_with_constraints(s + ")", o, c + 1)
        
        bt_with_constraints()
        return res
    
    #TLE approach
    def first_approach(self, n):
        s = list("(" * n + ")" * n)
        res = []
        temp = {}
        
        def check_is_valid (s):
            stack = []
            for element in list(s):
                if element == ')':
                    if stack:
                        stack.pop()
                else:
                    stack.append(element)
            
            return False if stack else True
        
            
        def backtrack(first):
            if s[0] == ')' or s[len(s) - 1] == '(':
                return
            
            s_str = ''.join(s)
            if first == len(s) and check_is_valid(s_str):
                if not s_str in temp:
                    res.append(s_str)
                    temp[s_str] = 1
                    return
                
            for i in range(first, len(s)):
                s[i], s[first] = s[first], s[i]
                backtrack(first + 1)
                s[i], s[first] = s[first], s[i]
        
        backtrack(0)
        return res
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack_with_constraint(n)
                
        

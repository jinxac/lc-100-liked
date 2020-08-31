class Solution:
    def brute_force(self, T):
        res = [0] * len(T)
        for i in range(len(T) - 1):
            for j in range(i+1, len(T)):
                if T[j] > T[i] and res[i] == 0:
                    res[i] = j - i
                
        return res

    def stack_approach_faster(self, T):
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
                
            stack.append(i)
        
        return res
        
    
    def stack_approach(self, T):        
        stack = []
        stack.append(T[0])
        i = 1
        j = i
        res = []
        
        while i < len(T) or j < len(T):
            if stack:
                ele = stack.pop()
            diff = 0
            if j < len(T) and ele >= T[j]:
                j += 1
            else:
                if j == len(T):
                    res.append(0)
                else:
                    res.append(j - i + 1)
                stack.append(T[i])
                i += 1
                j = i
                    
        res.append(0)
        return res
        
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # return self.brute_force(T)
        return self.stack_approach_faster(T)

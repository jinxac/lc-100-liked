class Solution:
    def recurse_backtrack(self, nums):
        res=[]
        def backtrack(first, temp):
            res.append(temp[:])
            for i in range(first, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()
        
        backtrack(0, [])
        return res
    
    def bottom_up_dp(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for curr in output:
                temp += [curr +[num]]
            output += temp
        
        return output
    
    def bitmask_approach(self, nums):
        n = len(nums)
        res = []
        cnt = 0 
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            temp = []
            for curr in range(len(bitmask)):
                if bitmask[curr] == '1':
                    temp.append(nums[curr])
            
            res.append(temp)
        
        return res
                    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.recurse_backtrack(nums)
        return self.bitmask_approach(nums)

class Solution:
    def iterative(self,nums):
        if not nums:
            return 0
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
    
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[len(nums) - 1]
    
    def recursive(nums):        
        if not nums:
            return 0
    
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def calculate(n):
            if n == 0:
                return nums[0]
            
            if n == 1:
                return max(nums[0], nums[1])
            
            return max(nums[n] + calculate(n-2), calculate(n-1))
                
        return calculate(len(nums) - 1)
    
    def rob(self, nums: List[int]) -> int:
        
        return self.recursive(nums)
        return self.iterative(nums)

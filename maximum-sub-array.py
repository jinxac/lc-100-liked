class Solution:
    def dp_with_space(self, nums):
        dp = [-10000000] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
    
    def dp_without_space(self, nums):
        global_max = curr_max = nums[0]
        
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(global_max, curr_max)
        
        return global_max

    def maxSubArray(self, nums: List[int]) -> int:
        return self.dp_without_space(nums)

class Solution:
    def optimised_space_approach(self, nums):
        l_nums = len(nums)
        L = [1] * l_nums
        R = 1
        
        for i in range(1, l_nums):
            L[i] = L[i-1] * nums[i-1]
        
        print(L)
        for i in reversed(range(l_nums)):
            L[i] = L[i] * R
            R = R * nums[i]
        
        return L
        
    
    
    def array_approach(self, nums):
        l_nums = len(nums)
        L = [1] * l_nums
        R = [1] * l_nums
        
        for i in range(1, l_nums):
            L[i] = L[i-1] * nums[i-1]
            
        for i in reversed(range(l_nums - 1)):
            R[i] = R[i+1] * nums[i+1]
        
        for i in range(l_nums):
            L[i] = L[i] * R[i]
        
        return L
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.array_approach(nums)
        return self.optimised_space_approach(nums)
        

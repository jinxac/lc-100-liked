class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
        
        ans = []
        # nums.extend([0] * cnt)
        
        i = 0
        
        while i < len(nums):
            if nums[i] != 0:
                ans.append(nums[i])
            i += 1
                
        while cnt > 0:
            ans.append(0)
            cnt -= 1
        
        i = 0
        while i < len(ans):
            nums[i] = ans[i]
            i += 1
        

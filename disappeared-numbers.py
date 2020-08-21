class Solution:
    def hash_map_approach(self, nums):
        temp_map= {x: 0 for x in range(1, len(nums) + 1)}
        res = []
        for element in nums:
            if element in temp_map:
                temp_map[element] += 1
        
        for key, val in temp_map.items():
            if val == 0:
                res.append(key)
            
        return res
    
    
    def smart_approach(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            ele = nums[abs(nums[i - 1]) - 1]
            if  ele > 0:
                nums[abs(nums[i - 1]) - 1] *= -1
        
        for i  in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res
    
    def set_approach(self, nums):
        curr_set = set(nums)
        actual_set = set([])
        for i in range(1, len(nums) + 1):
            actual_set.add(i)
        
        return actual_set - curr_set
        
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return self.hash_map_approach(nums)
        # return self.smart_approach(nums)
        return self.set_approach(nums)

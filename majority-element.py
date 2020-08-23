class Solution:
    def hash_map_approach(self, nums):
        len_nums = len(nums)
        temp_map = {x: nums.count(x) for x in set(nums)}
        
        for key, value in temp_map.items():
            if value > len_nums // 2:
                return key
        
        return None
        
     
    def center_element_approach(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
    
    def booyer_moore_voting(self, nums):
        count = 0 
        major_element = None
        
        for element in nums:
            if count == 0:
                major_element = element
            
            if major_element == element:
                count += 1
            else:
                count -= 1
        
        return major_element
    
    def majorityElement(self, nums: List[int]) -> int:
        # return self.hash_map_approach(nums)
        # return self.center_element_approach(nums)
        return self.booyer_moore_voting(nums)
        

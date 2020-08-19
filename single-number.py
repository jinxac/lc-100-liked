class Solution:
    def xor_approach(self,nums):
        res = 0
        for element in nums:
            res ^= element
        return res
    
    def hash_map_approach(self, nums):
        temp = {x: nums.count(x) for x in set(nums)}
        print(temp)
        for key, value in temp.items():
            if value == 1:
                return key
        
    def sum_approach(self, nums):
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber(self, nums: List[int]) -> int:
        # return self.xor_approach(nums)
        # return self.hash_map_approach(nums)
        return self.sum_approach(nums)

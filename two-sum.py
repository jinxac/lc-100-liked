class Solution:
    def brute_force(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j]
       
    
    def two_pass_hash(self, nums, target):
        temp = {element: i for i, element in enumerate(nums)}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if temp.get(diff) and temp.get(diff) != i:
                return [temp.get(diff), i]
    
    def single_pass_hash(self, nums, target):
        temp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in temp:
                return [temp[diff], i]
            else:
                temp[nums[i]] = i
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <2:
            return []
        return self.brute_force(nums, target)
        # return self.two_pass_hash(nums, target)
        return self.single_pass_hash(nums, target)

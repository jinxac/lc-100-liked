import heapq
from collections import Counter

class Solution:
    # TLE
    def my_approach(self, nums):
        if k == len(nums):
            return nums
        temp = {x: nums.count(x) for x in nums}
        h = []
        for key, value in temp.items():
            heapq.heappush(h, (value, key))
        
        res = []
        
        for element in heapq.nlargest(k, h):
            res.append(element[1])

        return res
    
    def nlargest_approach(self, nums, k):
        if k == len(nums):
            return nums
        temp = Counter(nums)
        return heapq.nlargest(k, temp.keys(), key = temp.get)
        
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.nlargest_approach(nums, k)

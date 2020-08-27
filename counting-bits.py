class Solution: 
    def nlogn_approach(self,num):
        def increment_content(nums):
            for i in range(len(nums)):
                nums[i] += 1
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        
        if num == 2:
            return [0,1,1]
        
        res = [0, 1, 1 ,2]
        temp = []
        temp_num = num
        while num > 2:
            a = res[:]
            increment_content(a)
            temp = a
            res.extend(temp)            
            temp = res
            
            num = num // 2
        
        return res[0:temp_num+1]
    
    def countBits(self, num: int) -> List[int]:
        return self.nlogn_approach(num)
        

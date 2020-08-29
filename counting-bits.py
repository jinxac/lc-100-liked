class Solution: 
    
    def hamming_approach(self, num):
        res = []
        def count_bits(x):
            cnt = 0
            while x:
                x &= x -1
                cnt += 1
            
            return cnt
        
        for i in range(num + 1):
            res.append(count_bits(i))
        
        return res
    
    
    def n_lsb_approach(self, num):
        dp = [0] * (num + 1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (i & 1)
        
        return dp
    
    
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
        # return self.nlogn_approach(num)
        # return self.hamming_approach(num)
        return self.n_lsb_approach(num)
        

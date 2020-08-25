class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if s[0] * len(s) == s:
            return 1
        
        i = 0
        j = 0
        res = 0
        temp_map = {}
        

        while j < len(s):
            if s[j] in temp_map:
                res = max(res, len(temp_map))
                temp_map = {}
                i += 1
                j = i
            else:
                temp_map[s[j]] = 1
                j += 1
        
        return max(res, len(temp_map))
        
                

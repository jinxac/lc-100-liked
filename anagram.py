class Solution:
    def hashmap_approach(self, strs):
        temp_map = {}
        for element in strs:
            count = [0] * 26
            for c in element:
                count[ord(c) - ord('a')] += 1
            
            count = str(count)
            if count in temp_map:
                temp_map[count].append(element)
            else:
                temp_map[count] = [element]
        
        return temp_map.values()
        
        
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.hashmap_approach(strs)
        

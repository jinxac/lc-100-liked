class Solution:
    def isValid(self, s: str) -> bool:
        # if not s:
        #     return True
        temp_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for element in s:
            if element in temp_map:
                top_element = "#"
                if len(stack):
                    top_element = stack.pop()
                
                if top_element != temp_map[element]:
                    return False
            else:
                stack.append(element)
            
            
        
        return len(stack) == 0

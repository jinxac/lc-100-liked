class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_element = 2147483649
        

    def push(self, x: int) -> None:
        self._stack.append(x)
        self._min_element = min(x, self._min_element)

    def pop(self) -> None:
        # TODO: Implement this in O(1)
        element = self._stack.pop()
        if element == self._min_element:
            self._min_element = 2147483649
            for element in self._stack:
                self._min_element = min(self._min_element, element)
        
        return element

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_element
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if not key in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        # print("here", len(self))
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

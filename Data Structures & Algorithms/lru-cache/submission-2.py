class LRUCache:

    def __init__(self, capacity: int):
        self.cap = deque()
        self.hashmap = defaultdict()
        self.capV = capacity
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        self.cap.remove(key)
        self.cap.append(key)
        return self.hashmap[key] 
        

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.hashmap[key] = value
            self.cap.remove(key)
            self.cap.append(key)
            return
        
        if len(self.cap) >= self.capV:
            curr = self.cap.popleft()
            del self.hashmap[curr]
        self.hashmap[key]=value
        self.cap.append(key)
        

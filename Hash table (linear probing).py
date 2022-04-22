class HashItem:    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key)


class HashTable:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.slots = [None for i in range(self.size)]
    
    def _hash(self, key):
        mult = 1
        hash_val = 0
        for c in key:
            hash_val += mult * ord(c)
            mult += 1
        return hash_val % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        slot = self._hash(key)        
        # collisions resolved by open addressing and linear probing
        while self.slots[slot] is not None:
            if self.slots[slot].key is key:
                break
            slot = (slot + 1) % self.size
        # if not overriding existing key, increase used slots counter by 1
        if self.slots[slot] is None:
            self.count += 1
        self.slots[slot] = item
        # expand table if getting full
        if self.count / self.size > 0.75:
            self.size *= 2
    
    def get(self, key):
        search_val = self._hash(key)
        while self.slots[search_val] is not None:
            if self.slots[search_val].key is key:
                return self.slots[search_val].value
            search_val = (search_val + 1) % self.size
        return None
    
    def remove(self, key):
        search_val = self._hash(key)
        while self.slots[search_val] is not None:
            if self.slots[search_val].key is key:
                del self.slots[search_val]
                self.count -= 1
            search_val = (search_val + 1) % self.size
        return None
    
    def __setitem__(self, key, value):
        self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)

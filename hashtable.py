

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h]element[1] == value

        self.arr[h].append((key, val))




    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    
t = HashTable()
print(t.get_hash("march 6"))
t.add("march 6", 130)
print(t.arr)
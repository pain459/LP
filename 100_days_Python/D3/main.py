class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def linear_probing(self, key, i):
        return (self.hash_function(key) + i) % self.size

    def insert(self, key, value):
        if self.count == self.size:
            raise Exception("Hash table is full")

        i = 0
        while i < self.size:
            index = self.linear_probing(key, i)
            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                self.count += 1
                return
            i += 1
        raise Exception("Unable to insert, table is full")

    def search(self, key):
        i = 0
        while i < self.size:
            index = self.linear_probing(key, i)
            if self.table[index] is None:
                return None
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
        return None

    def delete(self, key):
        i = 0
        while i < self.size:
            index = self.linear_probing(key, i)
            if self.table[index] is None:
                return False
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                self._rehash_from_index(index)
                return True
            i += 1
        return False

    def _rehash_from_index(self, start_index):
        i = (start_index + 1) % self.size
        while self.table[i] is not None:
            key, value = self.table[i]
            self.table[i] = None
            self.count -= 1
            self.insert(key, value)
            i = (i + 1) % self.size

    def __str__(self):
        return str([item for item in self.table if item is not None])

# Example usage
hash_table = HashTable()

# Inserting elements
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")
hash_table.insert("key4", "value4")
hash_table.insert("key5", "value5")
hash_table.insert("key6", "value6")
hash_table.insert("key7", "value7")
hash_table.insert("key8", "value8")
hash_table.insert("key9", "value9")

print("Hash Table:", hash_table)

# Searching for an element
print("Search for 'key2':", hash_table.search("key2"))

# Deleting an element
print("Delete 'key2':", hash_table.delete("key2"))
print("Hash Table after deletion:", hash_table)

# Searching for the deleted element
print("Search for 'key2':", hash_table.search("key2"))

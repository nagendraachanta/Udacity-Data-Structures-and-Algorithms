from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity=0):
        # Initialize class variables

        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache or self.capacity<=0:
            return -1
        # move the accessed key to the end of the dictionary.
        self.cache.move_to_end(key)
        return self.cache[key]


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        try:
            if len(self.cache) >= self.capacity:
                # first remove the least used item
                self.cache.popitem(last=False)
            self.cache[key] = value
        except KeyError:
            print("Invalid capacity declared")




# tests
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return -1


our_cache_edgecase=LRU_Cache(-1)
our_cache_edgecase.set(1, 1) # Invalid capacity declared
print(our_cache_edgecase.get(1)) # returns -1

our_cache_edgecase=LRU_Cache(0)
our_cache_edgecase.set(1, 1) # Invalid capacity declared
print(our_cache_edgecase.get(1)) # returns -1

from BOWInvertedIndexEngine import BOWInvertedIndexEngine
import pylru

class LRUCache(object):
    def __init__(self, size = 32):
        super().__init__()
        self.cache = pylru.lrucache(size)
    
    def has(self, key):
        return key in self.cache
    
    def get(self, key):
        return self.cache[key]
    
    def set(self, key, value):
        self.cache[key] = value
    
class BOWInvertedIndexEngineWIthCache(BOWInvertedIndexEngine.BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super().__init__()
    
    def search(self, query):
        if self.has(query):
            print('Cache hit!')
            return self.get(query)
        
        result = super().search(query)
        self.set(query, result)

        return result


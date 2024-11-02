#!/usr/bin/python3
"""implements a LRU caching system that stores in a dict"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and implements a LRU caching system"""

    def __init__(self):
        """ Initiliaze LIFOCache
        """
        super().__init__()
        self.lru_mapper = {}
        self.used_point = 0

    def put(self, key, item):
        """adds a item to the LIFO cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS) \
                    or (key in self.cache_data.keys()):
                self.cache_data[key] = item
                self.lru_mapper[key] = self.used_point
                self.used_point += 1
            else:
                lru_point = self.used_point
                discard_item_key = None
                # finds the key with least lru point
                for lru_key, point in self.lru_mapper.items():
                    if point < lru_point:
                        lru_point = point
                        discard_item_key = lru_key
                print(f"DISCARD: {discard_item_key}")
                del self.cache_data[discard_item_key]
                del self.lru_mapper[discard_item_key]
                self.cache_data[key] = item
                self.lru_mapper[key] = self.used_point
                self.used_point += 1

    def get(self, key):
        """Retrieves a given data from the cache using it's key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.lru_mapper[key] = self.used_point
        self.used_point += 1
        return self.cache_data.get(key, None)

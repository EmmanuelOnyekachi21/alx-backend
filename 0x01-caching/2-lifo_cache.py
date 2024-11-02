#!/usr/bin/python3
"""implements a LIFO caching system that stores in a dict"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements a LIFO caching system"""

    def __init__(self):
        """ Initiliaze LIFOCache
        """
        super().__init__()
        self.last_item = None

    def put(self, key, item):
        """adds a item to the LIFO cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS) \
                    or (key in self.cache_data.keys()):
                self.cache_data[key] = item
                self.last_item = key
            else:
                print(f"DISCARD: {self.last_item}")
                del self.cache_data[self.last_item]
                self.cache_data[key] = item
                self.last_item = key

    def get(self, key):
        """Retrieves a given data from the cache using it's key"""
        return self.cache_data.get(key, None)

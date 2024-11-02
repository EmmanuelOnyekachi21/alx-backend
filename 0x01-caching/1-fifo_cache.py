#!/usr/bin/python3
"""implements a FIFO caching system that stores in a dict"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits and implements a FIFO caching system"""

    def put(self, key, item):
        """adds a item to the FIFO cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS) \
                    or (key in self.cache_data.keys()):
                self.cache_data[key] = item
            else:
                for index, (c_key, val) in enumerate(self.cache_data.items()):
                    if index == 0:
                        first_item = c_key
                        break
                print(f"DISCARD: {first_item}")
                del (self.cache_data[first_item])
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves a given data from the cache using it's key"""
        return self.cache_data.get(key, None)

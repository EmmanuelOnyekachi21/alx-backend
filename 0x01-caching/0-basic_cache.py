#!/usr/bin/python3
"""implements a basic caching system that stores in a dict"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching, implementing a basic cache"""

    def put(self, key, item):
        """Adds to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a given data from the cache using it's key"""
        return self.cache_data.get(key, None)

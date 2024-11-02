#!/usr/bin/python3
"""implements a LFU caching system that stores in a dict"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and implements a LFU caching system"""

    def __init__(self):
        """ Initiliaze LIFOCache
        """
        super().__init__()
        self.lru_mapper = {}
        self.lfu_mapper = {}
        self.used_point = 0

    def put(self, key, item):
        """adds a item to the LIFO cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS) \
                    or (key in self.cache_data.keys()):
                if key not in self.cache_data.keys():
                    self.lfu_mapper[key] = 0
                else:
                    self.lfu_mapper[key] += 1
                self.cache_data[key] = item
                self.lru_mapper[key] = self.used_point
                self.used_point += 1
            else:
                lfU_val = list(self.lfu_mapper.values())[0]
                discard_item_key = None
                # finds minimal frequency
                for val in self.lfu_mapper.values():
                    if val < lfU_val:
                        lfU_val = val
                # creates a list of keys having the LFU valuue
                lfu_discard_list = [lfu_key for lfu_key, val in
                                    self.lfu_mapper.items() if val == lfU_val]
                if len(lfu_discard_list) == 1:
                    discard_item_key = lfu_discard_list[0]
                else:
                    lru_point = self.used_point
                    # finds the key with least lru point
                    for discard_key in lfu_discard_list:
                        point = self.lru_mapper[discard_key]
                        if point < lru_point:
                            lru_point = point
                            discard_item_key = discard_key
                print(f"DISCARD: {discard_item_key}")
                del self.cache_data[discard_item_key]
                del self.lru_mapper[discard_item_key]
                del self.lfu_mapper[discard_item_key]
                self.cache_data[key] = item
                self.lru_mapper[key] = self.used_point
                self.used_point += 1
                self.lfu_mapper[key] = 0

    def get(self, key):
        """Retrieves a given data from the cache using it's key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.lru_mapper[key] = self.used_point
        self.used_point += 1
        self.lfu_mapper[key] += 1
        return self.cache_data.get(key, None)

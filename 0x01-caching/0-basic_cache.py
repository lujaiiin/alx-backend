#!/usr/bin/python3
"""modules"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class"""
    def __init__(self):
        """ Init"""
        super().__init__()

    def put(self, key, item):
        """put"""
        if not key or not item:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """get"""
        return self.cache_data.get(key)

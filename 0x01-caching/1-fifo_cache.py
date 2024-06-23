#!/usr/bin/python3
"""modules"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class"""
    def __init__(self):
        """init"""
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """put"""
        if not key or not item:
            return
        if key not in self.__queue:
            self.__queue.append(key)
        if len(self.__queue) > self.MAX_ITEMS:
            self.cache_data.pop(self.__queue[0])
            print('DISCARD: {}'.format(self.__queue.pop(0)))
        self.cache_data.update({key: item})

    def get(self, key):
        """get"""
        return self.cache_data.get(key)

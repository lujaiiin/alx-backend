#!/usr/bin/python3
"""modules"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class"""
    def __init__(self):
        """init"""
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """put"""
        if not key or not item:
            return
        if key in self.__stack:
            self.__stack.remove(key)
        if len(self.__stack) == self.MAX_ITEMS:
            self.cache_data.pop(self.__stack[-1])
            print('DISCARD: {}'.format(self.__stack.pop()))
        self.__stack.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """get"""
        return self.cache_data.get(key)

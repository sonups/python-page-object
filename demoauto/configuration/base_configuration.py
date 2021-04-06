"""Represent the class for handling input yaml"""


class BaseConfiguration(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)
        self.__dict__ = self


global_data = BaseConfiguration(os=None, browser=None)

import csv
from abc import ABCMeta , abstractmethod

class Reader:
    __metaclass__ = ABCMeta

    def __init__(self ):
        pass

    @abstractmethod
    def readFile (self):
        pass
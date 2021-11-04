import math
from typing import List
from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def perform_search(self, array: List, column, query):
        pass

class startsWith(Filter):
    def perform_search(self, array: List, column, query):
        temp = []
        for idx in range(0 , len(array)):
            string = array[idx].all_attributes[column]
            if query == string[0]:
                temp.append(array[idx])
        
        return temp
from typing import List
from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def perform_search(self, array: List, column, query):
        pass


class startsWith(Filter):
    def perform_search(self, array: List, column, query):
        temp = []
        for idx in range(0, len(array)):
            string = array[idx].all_attributes[column]
            string = str(string)
            query = str(query)
            if (
                query == string[0]
                or query.capitalize == string[0]
                or query.lower == string[0]
            ):
                temp.append(array[idx])
        return temp


class endsWith(Filter):
    def perform_search(self, array: List, column, query):
        temp = []
        for idx in range(0, len(array)):
            string = array[idx].all_attributes[column]
            string = str(string)
            query = str(query)
            if (
                query == string[len(string) - 1]
                or query.capitalize() == string[len(string) - 1]
                or query.lower() == string[len(string) - 1]
            ):
                temp.append(array[idx])
        return temp


class contains(Filter):
    def perform_search(self, array: List, column, query):
        temp = []
        for idx in range(0, len(array)):
            string = array[idx].all_attributes[column]
            string = str(string)
            query = str(query)
            if (
                query in string
                or query.lower() in string
                or query.capitalize() in string
            ):
                temp.append(array[idx])
        return temp


class doesNotContain(Filter):
    def perform_search(self, array: List, column, query):
        temp = []
        for idx in range(0, len(array)):
            string = array[idx].all_attributes[column]
            string = str(string)
            query = str(query)
            if (
                query not in string
                or query.lower() not in string
                or query.capitalize() not in string
            ):
                temp.append(array[idx])

        print("LengthTemp:", len(temp))
        return temp

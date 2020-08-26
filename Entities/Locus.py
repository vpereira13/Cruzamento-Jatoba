"""
Classe de locus:
    Contém uma dupla de genes (tripla de inteiros)
    first  - primeira parte do locus, uma string formada por três inteiros
    second - segunda parte do locus, uma string formada por três inteiros
"""


class Locus:
    def __init__(self, first: str, second: str):
        if len(first) == 3 and first.isdigit():
            self.__first = first
        if len(second) == 3 and second.isdigit():
            self.__second = second

    def get_first(self):
        return self.__first

    def get_second(self):
        return self.__second

    def is_zero(self):
        return self.__first == "000" and self.__second == "000"

    def __str__(self):
        return "{}\t{}".format(self.__first, self.__second)

"""
Classe de loci:
    Coleção de 8 locus
"""
from Entities.Locus import Locus


class Loci:
    __collector = []

    def add(self, locus: Locus):
        if len(self.__collector) < 9:
            self.__collector.append(locus)

    def all(self):
        return self.__collector

    def clear(self):
        self.__collector = []

    def __str__(self):
        return "\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format(
            str(self.__collector[0]),
            str(self.__collector[1]),
            str(self.__collector[2]),
            str(self.__collector[3]),
            str(self.__collector[4]),
            str(self.__collector[5]),
            str(self.__collector[6]),
            str(self.__collector[7]),
        )

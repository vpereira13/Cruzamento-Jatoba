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

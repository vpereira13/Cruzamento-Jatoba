"""
Classe de loci:
    Coleção de 8 locus
"""
from Entities.Locus import Locus
from data.settings import N_LOCUS_IN_LOCI


class Loci:
    __collector = []

    def add(self, locus: Locus):
        if len(self.__collector) < N_LOCUS_IN_LOCI + 1:
            self.__collector.append(locus)

    def all(self):
        return self.__collector

    def clear(self):
        self.__collector = []

    def __str__(self):
        loci_str = ""
        for locus in self.__collector:
            loci_str += str(locus) + "\t"
        return loci_str[:-1]

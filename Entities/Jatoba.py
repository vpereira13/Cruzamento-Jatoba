from Entities.Location import Location
from Entities.Loci import Loci


class Jatoba:
    """
    Classe de cada jatobazeiro:
        identifier  - id do indivíduo
        age         - Idade
        x           - Localização do indivíduo, eixo X
        y           - Localização do indivíduo, eixo Y
        loci        - Conjunto de locus
        fatherid    - id do pai (pode não existir se for gerado por
                      autofecundação ou se for carregado do arquivo)
        motherid    - id da mãe (pode não existir se for carregado do arquivo)
    """

    def __init__(self):
        pass

    def set_identifier(self, identifier: int):
        self.__identifier = identifier

    def set_age(self, age: int):
        self.__age = age

    def set_location(self, location: Location):
        self.__location = location

    def set_loci(self, loci: Loci):
        self.__loci = loci

    def get_identifier(self):
        return self.__identifier

    def get_age(self):
        return self.__age

    def get_location(self):
        return self.__location

    def get_loci(self):
        return self.__loci

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(
            str(self.__identifier),
            str(self.__age),
            str(self.__location),
            str(self.__loci)
        )

import secrets

from Entities.Jatoba import Jatoba
from Entities.Loci import Loci
from Entities.Locus import Locus


def locus_generator(locus_a: Locus, locus_b: Locus = None):
    first = "{0:02b}".format(secrets.randbits(2))
    second = "{0:02b}".format(secrets.randbits(2))

    if locus_b is None:
        # Somente mãe
        return Locus(
            locus_a.get_first() if first[0] == '1' else locus_a.get_second(),
            locus_a.get_first() if second[0] == '1' else locus_a.get_second()
        )

    if locus_a.is_zero() or locus_b.is_zero():
        # Caso de mãe ou pai com zero
        return Locus("000", "000")

    # Caso cruzado
    #                  |   locus.first    |   locus.second   |
    #                  |     (filho)      |      (filho)     |
    # ---------------------------------------------------------
    #  locus_a.first   |    first = 11    |    second = 11   |
    #  locus_a.second  |    first = 10    |    second = 10   |
    #  locus_b.first   |    first = 01    |    second = 01   |
    #  locus_b.second  |    first = 00    |    second = 00   |
    #
    return Locus(
        locus_a.get_first() if first[0] == '1' and first[1] == '1' else
        locus_a.get_second() if first[0] == '1' and first[1] == '0' else
        locus_b.get_first() if first[0] == '0' and first[1] == '1' else
        locus_b.get_second(),
        locus_a.get_first() if second[0] == '1' and second[1] == '1' else
        locus_a.get_second() if second[0] == '1' and second[1] == '0' else
        locus_b.get_first() if second[0] == '0' and second[1] == '1' else
        locus_b.get_second()
    )


def self_fertilization(jatoba: Jatoba):
    loci = Loci()
    for i in jatoba.get_loci().all():
        loci.add(locus_generator(i))
    return loci


def cross_fertilization(mother: Jatoba, father: Jatoba):
    loci = Loci()
    for i in range(len(mother.get_loci().all())):
        loci.add(locus_generator(mother.get_loci().all()[i], father.get_loci().all()[i]))
    return loci

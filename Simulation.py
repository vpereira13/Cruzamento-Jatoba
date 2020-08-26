import secrets
import logging
import logging.config
from Collections.JatobaPopulation import JatobaPopulation
from Entities.Location import Location
from Entities.Jatoba import Jatoba
from Entities.Loci import Loci
from Entities.Locus import Locus
from Resolvers import LocationResolver, FecundationResolver, RecordPopulationResolver
from data.settings import YEAR_MAX, MATCHES, SELF_FECUNDATION_RATE, INPUT_FILENAME, CHECKPOINT_PERIODICITY


def load_initial_population():
    data = open('data/Input/' + INPUT_FILENAME, 'r')

    population = JatobaPopulation()
    for line in data:
        parameters = line.replace('\n', '').split('\t')
        jatoba = Jatoba()
        location = Location()
        location.set_x(int(parameters[2]))
        location.set_y(int(parameters[3]))
        loci = Loci()
        loci.clear()
        for i in range(4, 20, 2):
            locus = Locus(parameters[i], parameters[i + 1])
            loci.add(locus)
        jatoba.set_identifier(int(parameters[0]))
        jatoba.set_age(int(parameters[1]))
        jatoba.set_location(location)
        jatoba.set_loci(loci)
        population.add(jatoba)
    data.close()

    return population


def main():
    logger = logging.getLogger('jatoba-simulation')
    logger.info("Início da simulação")

    logger.debug("Iniciando o carregamento da população inicial")
    population = load_initial_population()
    logger.debug("Término do carregamento da população inicial")

    for year in range(YEAR_MAX):
        if population.size() == 0:
            logger.debug("Não há mais indivíduos. Finalizando execução.")
            exit(0)

        n_matches = secrets.randbelow(MATCHES)

        logger.debug("Iniciando ano %d. Terá %d cruzamentos", year + 1, n_matches)

        for match in range(n_matches):
            # Verifies that there is at least one adult in population
            # if doesn't exists, pass a year
            if population.is_there_an_adult() is False:
                logger.debug("Não há adultos, então não haverá cruzamento esse ano")
                break

            # 97,3% normal match, 2,7% self-fertilization
            match_type = secrets.randbelow(1000)

            new_jatoba = Jatoba()
            new_jatoba.set_identifier(id(new_jatoba))
            new_jatoba.set_age(0)
            new_jatoba.set_location(LocationResolver.generate_random_location())

            # self-fertilization case
            if match_type < SELF_FECUNDATION_RATE:
                mother = population.select_random_jatoba()
                logger.debug("Cruzamento de auto fecundação. Indivíduo: %d", mother.get_identifier())

                new_jatoba.set_loci(FecundationResolver.self_fertilization(mother))

            # cross fertilization case
            else:
                mother = population.select_random_jatoba()
                father = population.select_random_jatoba(mother.get_identifier())

                logger.debug(
                    "Cruzamento de dois indivíduos. Indivíduos: %d, %d",
                    mother.get_identifier(),
                    father.get_identifier()
                )
                new_jatoba.set_loci(FecundationResolver.cross_fertilization(mother, father))

            population.add(new_jatoba)

        # Death time
        logger.debug("Sopro da morte. Tamanho da população atual: %d", population.size())
        population.death_blow()
        logger.debug("Tamanho da população sobrevivente: %d", population.size())

        # Birthday time
        logger.debug("Término do ano. Todos fazem aniversário")
        for jatoba in population.all():
            jatoba.birthday()

        if (year + 1) % CHECKPOINT_PERIODICITY == 0:
            logger.debug("Ano: {}. Salvando a população".format(year + 1))
            RecordPopulationResolver.save_population(population, year + 1)

    RecordPopulationResolver.save_population(population)

    logger.info("Término da simulação")


if __name__ == '__main__':
    logging.config.fileConfig('app/Logger/logging.conf')
    main()

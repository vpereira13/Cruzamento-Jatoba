from datetime import datetime
from Collections.JatobaPopulation import JatobaPopulation


def save_population(population: JatobaPopulation, year: int = None):
    if population.size() == 0:
        exit(0)

    now = datetime.now()
    if year is not None:
        with open('data/Results/year{}_{}.out'.format(year, now), 'w') as f:
            for jatoba in population.all():
                print(jatoba, file=f)
    else:
        with open('data/Results/final{}.out'.format(now), 'w') as f:
            for jatoba in population.all():
                print(jatoba, file=f)

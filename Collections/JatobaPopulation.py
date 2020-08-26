import secrets
from Entities.Jatoba import Jatoba


class JatobaPopulation:
    __collector = []

    def add(self, jatoba: Jatoba):
        self.__collector.append(jatoba)

    def all(self):
        return self.__collector

    def size(self):
        return len(self.__collector)

    def is_there_an_adult(self):
        for jatoba in self.__collector:
            if jatoba.get_age() > 25:
                return True
        return False

    def death_blow(self):
        i = 0
        n = len(self.__collector)

        while i < n:
            rnd = int(secrets.randbelow(1000))
            age = self.__collector[i].get_age()

            if age == 0:
                if rnd < 980:
                    self.__collector.pop(i)
                    i -= 1
            elif age < 21:
                if rnd < 460:
                    self.__collector.pop(i)
                    i -= 1
            elif age < 150:
                if rnd < 100:
                    self.__collector.pop(i)
                    i -= 1
            else:
                self.__collector.pop(i)
                i -= 1
            i += 1
            n = len(self.__collector)

    def select_random_jatoba(self, mother_id=None):
        population_size = self.size()
        n = secrets.randbelow(population_size)

        if mother_id is None:
            while self.__collector[n].get_age() < 25:
                n = secrets.randbelow(population_size)
        else:
            while self.__collector[n].get_age() < 25 and self.__collector[n].get_identifier() != mother_id:
                n = secrets.randbelow(population_size)

        return self.__collector[n]

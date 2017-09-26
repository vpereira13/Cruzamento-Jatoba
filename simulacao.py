import secrets

DATAIN  = "data.in"
AREA    = "A"
YEARMAX = 500
MATCHES = 1000
Xi      = 30
Xf      = 30000
Yi      = 30
Yf      = 30000
ID      = 0
AGE     = 1
X       = 2
Y       = 3
LOCUS11 = 4
LOCUS12 = 5
LOCUS21 = 6
LOCUS22 = 7
LOCUS31 = 8
LOCUS32 = 9
LOCUS41 = 10
LOCUS42 = 11
LOCUS51 = 12
LOCUS52 = 13
LOCUS61 = 14
LOCUS62 = 15
LOCUS71 = 16
LOCUS72 = 17
LOCUS81 = 18
LOCUS82 = 19


def generateRandomLocation(initial, final):
    return initial + secrets.randbelow(final - initial)

def thereIsZero(motherLocus, fatherLocus):
    return True if motherLocus.getFirst() is '000' or fatherLocus.getFirst() is '000' else False

def generateLoci(mother, father=None):
    rnd  = "{0:016b}".format(secrets.randbits(16))
    rnd2 = "{0:016b}".format(secrets.randbits(16))
    if father is None:
        loci = Loci(Locus(mother.getLoci().getLoci()[0].getFirst() if not rnd[ 0] else mother.getLoci().getLoci()[0].getSecond(),
                          mother.getLoci().getLoci()[0].getFirst() if not rnd[ 1] else mother.getLoci().getLoci()[0].getSecond()),
                    Locus(mother.getLoci().getLoci()[1].getFirst() if not rnd[ 2] else mother.getLoci().getLoci()[1].getSecond(),
                          mother.getLoci().getLoci()[1].getFirst() if not rnd[ 3] else mother.getLoci().getLoci()[1].getSecond()),
                    Locus(mother.getLoci().getLoci()[2].getFirst() if not rnd[ 4] else mother.getLoci().getLoci()[2].getSecond(),
                          mother.getLoci().getLoci()[2].getFirst() if not rnd[ 5] else mother.getLoci().getLoci()[2].getSecond()),
                    Locus(mother.getLoci().getLoci()[3].getFirst() if not rnd[ 6] else mother.getLoci().getLoci()[3].getSecond(),
                          mother.getLoci().getLoci()[3].getFirst() if not rnd[ 7] else mother.getLoci().getLoci()[3].getSecond()),
                    Locus(mother.getLoci().getLoci()[4].getFirst() if not rnd[ 8] else mother.getLoci().getLoci()[4].getSecond(),
                          mother.getLoci().getLoci()[4].getFirst() if not rnd[ 9] else mother.getLoci().getLoci()[4].getSecond()),
                    Locus(mother.getLoci().getLoci()[5].getFirst() if not rnd[10] else mother.getLoci().getLoci()[5].getSecond(),
                          mother.getLoci().getLoci()[5].getFirst() if not rnd[11] else mother.getLoci().getLoci()[5].getSecond()),
                    Locus(mother.getLoci().getLoci()[6].getFirst() if not rnd[12] else mother.getLoci().getLoci()[6].getSecond(),
                          mother.getLoci().getLoci()[6].getFirst() if not rnd[13] else mother.getLoci().getLoci()[6].getSecond()),
                    Locus(mother.getLoci().getLoci()[7].getFirst() if not rnd[14] else mother.getLoci().getLoci()[7].getSecond(),
                          mother.getLoci().getLoci()[7].getFirst() if not rnd[15] else mother.getLoci().getLoci()[7].getSecond()))

    else:
        loci = Loci(Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[0], father.getLoci().getLoci()[0]) else
                    Locus(mother.getLoci().getLoci()[0].getFirst()  if not rnd[0] and not rnd2[0] else
                          mother.getLoci().getLoci()[0].getSecond() if not rnd[0] and     rnd2[0] else
                          father.getLoci().getLoci()[0].getFirst()  if     rnd[0] and not rnd2[0] else
                          father.getLoci().getLoci()[0].getSecond(),
                          mother.getLoci().getLoci()[0].getFirst()  if not rnd[1] and not rnd2[1] else
                          mother.getLoci().getLoci()[0].getSecond() if not rnd[1] and     rnd2[1] else
                          father.getLoci().getLoci()[0].getFirst()  if     rnd[1] and not rnd2[1] else
                          father.getLoci().getLoci()[0].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[1], father.getLoci().getLoci()[1]) else
                    Locus(mother.getLoci().getLoci()[1].getFirst()  if not rnd[2] and not rnd2[2] else
                          mother.getLoci().getLoci()[1].getSecond() if not rnd[2] and     rnd2[2] else
                          father.getLoci().getLoci()[1].getFirst()  if     rnd[2] and not rnd2[2] else
                          father.getLoci().getLoci()[1].getSecond(),
                          mother.getLoci().getLoci()[1].getFirst()  if not rnd[3] and not rnd2[3] else
                          mother.getLoci().getLoci()[1].getSecond() if not rnd[3] and     rnd2[3] else
                          father.getLoci().getLoci()[1].getFirst()  if     rnd[3] and not rnd2[3] else
                          father.getLoci().getLoci()[1].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[2], father.getLoci().getLoci()[2]) else
                    Locus(mother.getLoci().getLoci()[2].getFirst()  if not rnd[4] and not rnd2[4] else
                          mother.getLoci().getLoci()[2].getSecond() if not rnd[4] and     rnd2[4] else
                          father.getLoci().getLoci()[2].getFirst()  if     rnd[4] and not rnd2[4] else
                          father.getLoci().getLoci()[2].getSecond(),
                          mother.getLoci().getLoci()[2].getFirst()  if not rnd[5] and not rnd2[5] else
                          mother.getLoci().getLoci()[2].getSecond() if not rnd[5] and     rnd2[5] else
                          father.getLoci().getLoci()[2].getFirst()  if     rnd[5] and not rnd2[5] else
                          father.getLoci().getLoci()[2].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[3], father.getLoci().getLoci()[3]) else
                    Locus(mother.getLoci().getLoci()[3].getFirst()  if not rnd[6] and not rnd2[6] else
                          mother.getLoci().getLoci()[3].getSecond() if not rnd[6] and     rnd2[6] else
                          father.getLoci().getLoci()[3].getFirst()  if     rnd[6] and not rnd2[6] else
                          father.getLoci().getLoci()[3].getSecond(),
                          mother.getLoci().getLoci()[3].getFirst()  if not rnd[7] and not rnd2[7] else
                          mother.getLoci().getLoci()[3].getSecond() if not rnd[7] and     rnd2[7] else
                          father.getLoci().getLoci()[3].getFirst()  if     rnd[7] and not rnd2[7] else
                          father.getLoci().getLoci()[3].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[4], father.getLoci().getLoci()[4]) else
                    Locus(mother.getLoci().getLoci()[4].getFirst()  if not rnd[8] and not rnd2[8] else
                          mother.getLoci().getLoci()[4].getSecond() if not rnd[8] and     rnd2[8] else
                          father.getLoci().getLoci()[4].getFirst()  if     rnd[8] and not rnd2[8] else
                          father.getLoci().getLoci()[4].getSecond(),
                          mother.getLoci().getLoci()[4].getFirst()  if not rnd[9] and not rnd2[9] else
                          mother.getLoci().getLoci()[4].getSecond() if not rnd[9] and     rnd2[9] else
                          father.getLoci().getLoci()[4].getFirst()  if     rnd[9] and not rnd2[9] else
                          father.getLoci().getLoci()[4].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[5], father.getLoci().getLoci()[5]) else
                    Locus(mother.getLoci().getLoci()[5].getFirst()  if not rnd[10] and not rnd2[10] else
                          mother.getLoci().getLoci()[5].getSecond() if not rnd[10] and     rnd2[10] else
                          father.getLoci().getLoci()[5].getFirst()  if     rnd[10] and not rnd2[10] else
                          father.getLoci().getLoci()[5].getSecond(),
                          mother.getLoci().getLoci()[5].getFirst()  if not rnd[11] and not rnd2[11] else
                          mother.getLoci().getLoci()[5].getSecond() if not rnd[11] and     rnd2[11] else
                          father.getLoci().getLoci()[5].getFirst()  if     rnd[11] and not rnd2[11] else
                          father.getLoci().getLoci()[5].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[6], father.getLoci().getLoci()[6]) else
                    Locus(mother.getLoci().getLoci()[6].getFirst()  if not rnd[12] and not rnd2[12] else
                          mother.getLoci().getLoci()[6].getSecond() if not rnd[12] and     rnd2[12] else
                          father.getLoci().getLoci()[6].getFirst()  if     rnd[12] and not rnd2[12] else
                          father.getLoci().getLoci()[6].getSecond(),
                          mother.getLoci().getLoci()[6].getFirst()  if not rnd[13] and not rnd2[13] else
                          mother.getLoci().getLoci()[6].getSecond() if not rnd[13] and     rnd2[13] else
                          father.getLoci().getLoci()[6].getFirst()  if     rnd[13] and not rnd2[13] else
                          father.getLoci().getLoci()[6].getSecond()),
                    Locus('000', '000') if thereIsZero(mother.getLoci().getLoci()[7], father.getLoci().getLoci()[7]) else
                    Locus(mother.getLoci().getLoci()[7].getFirst()  if not rnd[14] and not rnd2[14] else
                          mother.getLoci().getLoci()[7].getSecond() if not rnd[14] and     rnd2[14] else
                          father.getLoci().getLoci()[7].getFirst()  if     rnd[14] and not rnd2[14] else
                          father.getLoci().getLoci()[7].getSecond(),
                          mother.getLoci().getLoci()[7].getFirst()  if not rnd[15] and not rnd2[15] else
                          mother.getLoci().getLoci()[7].getSecond() if not rnd[15] and     rnd2[15] else
                          father.getLoci().getLoci()[7].getFirst()  if     rnd[15] and not rnd2[15] else
                          father.getLoci().getLoci()[7].getSecond()))
    return loci

'''
	Função para retornar se há um indivíduo adult em uma população,
	útil para saber se ele é fértil.

	Parametros:
		population - populacao, um conjunto de indivíduos

	Retorno:
		True - se existe um indivíduo na população
		False - caso não existir
'''
def thereIsAnAdult(population):
    for ind in population:
        if ind.getAge() > 25:
           return True
    return False

def selectRandomIndividual(population, motherID=None):
    n = secrets.randbelow(len(population))

    if motherID is None:
        while population[n].getAge() < 25:
            n = secrets.randbelow(len(population))
    else:
        while population[n].getAge() < 25 and population[n].getID() != motherID:
            n = secrets.randbelow(len(population))

    return population[n]

'''
Classe de locus:
    Contém uma dupla de genes, formado por um inteiro de 3 dígitos
'''
class Locus:
    # creation
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    # getters
    def getFirst(self):
        return self.__first

    def getSecond(self):
        return self.__second

    def getLocus(self):
        return self.__first, self.__second

    def printLocus(self):
        print(self.__first+"\t"+self.__second)

'''
Classe de loci:
    Conjunto com 8 unidades de locus
'''
class Loci:
    #creation
    def __init__(self, locus1, locus2, locus3, locus4,
                 locus5, locus6, locus7, locus8):
        self.__locus1 = locus1
        self.__locus2 = locus2
        self.__locus3 = locus3
        self.__locus4 = locus4
        self.__locus5 = locus5
        self.__locus6 = locus6
        self.__locus7 = locus7
        self.__locus8 = locus8

    #getters
    def getLoci(self):
        return self.__locus1, self.__locus2, self.__locus3, self.__locus4,\
               self.__locus5, self.__locus6, self.__locus7, self.__locus8

    def printLoci(self):
        print("locus 1:", end="\t")
        self.__locus1.printLocus()
        print("locus 2:", end="\t")
        self.__locus2.printLocus()
        print("locus 3:", end="\t")
        self.__locus3.printLocus()
        print("locus 4:", end="\t")
        self.__locus4.printLocus()
        print("locus 5:", end="\t")
        self.__locus5.printLocus()
        print("locus 6:", end="\t")
        self.__locus6.printLocus()
        print("locus 7:", end="\t")
        self.__locus7.printLocus()
        print("locus 8:", end="\t")
        self.__locus8.printLocus()


'''
Classe de indivíduo:
    ID          - ID do indivíduo
    age         - Idade do indivíduo
    x           - Localização do indivíduo, eixo X
    y           - Localização do indivíduo, eixo Y
    loci        - Conjunto de locus
    fatherID    - ID do pai (pode não existir se for gerado por autofecundação ou se for carregado do arquivo)
    motherID    - ID da mãe (pode não existir se for carregado do arquivo)
'''
class Individual:
    # creation
    def __init__(self, year, count=None, id=None, age=None, x=None, y=None, loci=None, fatherID=None, motherID=None):
        if id is None and count is not None:
            self.__id = AREA + str(year) + str(count)
        else:
            self.__id = id

        if age is None:
            self.__age = int(0)
        else:
            self.__age = int(age)

        if x is None:
            self.__x = int(generateRandomLocation(Xi, Xf))
        else:
            self.__x = int(x)

        if x is None:
            self.__y = int(generateRandomLocation(Yi, Yf))
        else:
            self.__y = int(y)

        if loci is None:
            if fatherID is None:
                if motherID is None:
                    self.__motherID = 0
                    self.__fatherID = 0
                else:
                    self.__loci = generateLoci(motherID)
            else:
                self.__loci = generateLoci(motherID, fatherID)
        else:
            self.__loci = loci

        self.__fatherID = fatherID
        self.__motherID = motherID

    # getters
    def getID(self):
        return self.__id

    def getAge(self):
        return int(self.__age)

    def getX(self):
        return int(self.__x)

    def getY(self):
        return int(self.__y)

    def getFatherID(self):
        return self.__fatherID

    def getMotherID(self):
        return self.__motherID

    def getLoci(self):
        return self.__loci

    def printIndividual(self):
        print("ID:\t" + self.__id)
        print("Age:\t" + str(self.__age))
        print("X:\t" + str(self.__x))
        print("Y:\t" + str(self.__y))
        if self.__fatherID is not None:
            print("FatherID:\t" + self.__fatherID)
        else:
            print("FatherID:\t--")
        if self.__fatherID is not None:
            print("MotherID:\t" + self.__motherID)
        else:
            print("MotherID:\t--")
        self.__loci.printLoci()
        print()

    def birthday(self):
        self.__age += 1

def deathBlow(population):
    i = 0
    n = len(population)

    while i < n:
        rnd = int(secrets.randbelow(1000))

        if population[i].getAge() == 0:
            if rnd < 980:
                population.pop(i)
                i -= 1
        elif population[i].getAge() < 21:
            if rnd < 460:
                population.pop(i)
                i -= 1
        elif population[i].getAge() < 150:
            if rnd < 100:
                population.pop(i)
                i -= 1
        else:
            population.pop(i)
            i -= 1
        i += 1
        n = len(population)

# Load base file data
data = open(DATAIN, 'r')
population = []
for line in data:
    parameters = line.replace('\n','').split('\t')
    new = Individual(0, None, parameters[ID], parameters[AGE], parameters[X], parameters[Y],
                     Loci(Locus(parameters[LOCUS11], parameters[LOCUS12]),
                          Locus(parameters[LOCUS21], parameters[LOCUS22]),
                          Locus(parameters[LOCUS31], parameters[LOCUS32]),
                          Locus(parameters[LOCUS41], parameters[LOCUS42]),
                          Locus(parameters[LOCUS51], parameters[LOCUS52]),
                          Locus(parameters[LOCUS61], parameters[LOCUS62]),
                          Locus(parameters[LOCUS71], parameters[LOCUS72]),
                          Locus(parameters[LOCUS81], parameters[LOCUS82])))
    population.append(new)
data.close()

# Simulation
if __name__ == "__main__":
		for year in range(YEARMAX):
			print("Ano: " + str(year) + "\tPopulação: " + str(len(population)))
			COUNT = 0

			nMatches = secrets.randbelow(MATCHES)
			for match in range(nMatches):
				# Verifies that there is at least one adult in population
				# if doesn't exists, pass a year
				if thereIsAnAdult(population) is False:
					break
				else:
					# 97,3% normal match, 2,7% self-fertilization
					matchType = secrets.randbelow(1000)

					# self-fertilization case
					if matchType < 27:
						mother = selectRandomIndividual(population)
						new = Individual(year, COUNT, None, 0, generateRandomLocation(Xi, Xf), generateRandomLocation(Yi, Yf),
										 generateLoci(mother), None, mother.getID())
						population.append(new)

					# normal fertilization case
					else:
						mother = selectRandomIndividual(population)
						father = selectRandomIndividual(population, mother.getID())
						new = Individual(year, COUNT, None, 0, generateRandomLocation(Xi, Xf), generateRandomLocation(Yi, Yf),
										 generateLoci(mother, father), father.getID(), mother.getID())
						population.append(new)

					COUNT += 1

				# Death time
				deathBlow(population)

				# Birthday time
				for ind in population:
					ind.birthday()

				# Save population in output files
				if year == 9 or year == 19 or year == 49 or year == 99 or year == 199 or year == 249 or year == 399 or year == 499:
					outputFile = open(str(year)+'.out','w')
			        for ind in population:
            			for j in i:
			                saida.write(str(j) + '\t')
            				saida.write('\n')
			        saida.close()

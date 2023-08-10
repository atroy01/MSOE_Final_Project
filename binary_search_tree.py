# Binary Search Tree classes for Project 10
# Andrew Troy
# 2023-08-09

class Country(object):  # One part of the data Tree
    def __init__(self, population: int, name: str, other_data=[]):  # Constructor
        self.population = population  # the population of the country. This is the key for the BST
        self.name = name
        self.other_data = other_data
        self.left = None  # the left child
        self.right = None  # the right child

    def __str__(self):
        return self.name


class PopulationNode(object):  # One part of the data Tree
    def __init__(self, population: int, countries=[]):  # Constructor
        self.population = population  # the population of the country. This is the key for the BST
        self.left = None  # the left child
        self.right = None  # the right child
        self.countries = countries

    def __str__(self):
        country_names = ', '.join(country.name for country in self.countries)
        return f'{self.population}: {country_names}'


class PopulationBST(object):  # A binary search tree of data elements
    def __init__(self):  # Constructor
        self.root = None  # Reference to start of BST
        self.size = 0  # variable to keep track of the size of the tree

    def addCountry(self, country: Country):
        self.size += 1
        if not self.root:
            self.root = PopulationNode(country.population, [country])  # if no root exists, then create a new PopulationNode with one country in it
        else:
            self._addCountry(self.root, country)
        # # TODO: I think here we need to simultaneously add a country to the CountryBST
        # countryBST.addCountry(country)
        return

    def _addCountry(self, cur: PopulationNode, countryToAdd: Country):  # this is the recursive form of the function
        if countryToAdd.population < cur.population:
            if cur.left:
                self._addCountry(cur.left, countryToAdd)
            else:  # the left PopulationNode does not exist, so we can add this PopulationNode there
                cur.left = PopulationNode(countryToAdd.population, [countryToAdd])  # if no root exists, then create a new PopulationNode with one country in it
        if countryToAdd.population > cur.population:
            if cur.right:
                self._addCountry(cur.right, countryToAdd)
            else:  # the right PopulationNode does not exist, so we can add this PopulationNode there
                cur.right = PopulationNode(countryToAdd.population, [countryToAdd])  # if no root exists, then create a new PopulationNode with one country in it
        if countryToAdd.population == cur.population:  # special case where the population of the country being added is already within the tree
            cur.countries.append(countryToAdd)  # append the country to the countries list

    def findCountryFromPopulation(self, population: int):
        print(f'Looking for country with population of {population}.')
        if not self.root:
            print('No tree exists')
        else:
            self._findCountryFromPopulation(self.root, population, None, None)
        return

    def _findCountryFromPopulation(self, cur: PopulationNode, population: int, lastLeft: PopulationNode, lastRight: PopulationNode,):
        if population > cur.population:
            if cur.right:
                self._findCountryFromPopulation(cur.right, population, lastLeft, cur)
            else:
                lastRight = cur
                print(f'   Not an exact match, but next smallest is {lastRight}, and next largest is {lastLeft}')
                return
        elif population < cur.population:
            if cur.left:
                self._findCountryFromPopulation(cur.left, population, cur, lastRight)
            else:
                lastLeft = cur
                print(f'   Not an exact match, but next smallest is {lastRight}, and next largest is {lastLeft}')
                return
        elif population == cur.population:
            print(f'   Found a match with that population size: {cur}')
            return


    def printLargestToSmallest(self, cur):
        if cur.right:
            self.printLargestToSmallest(cur.right)
        print(cur)
        if cur.left:
            self.printLargestToSmallest(cur.left)

    def __str__(self):
        self.printLargestToSmallest(self.root)
        return ''


class CountryBST(object):  # A binary search tree of data elements
    def __init__(self):  # Constructor
        self.root = None  # Reference to start of BST
        self.size = 0  # variable to keep track of the size of the tree

    def addCountry(self, country: Country):  # this is the starter form to check if the roo exists
        self.size += 1
        if not self.root:
            self.root = country  # if no root exists, then make the passed country the root
        else:
            self._addCountry(self.root, country)  # enter the recursive function
        return

    def _addCountry(self, cur: Country, countryToAdd: Country):  # this is the recursive form of the function
        if countryToAdd.name < cur.name:
            if cur.left:
                self._addCountry(cur.left, countryToAdd)
            else:  # the left Country does not exist, so we can add this Country there
                cur.left = countryToAdd
        if countryToAdd.name > cur.name:
            if cur.right:
                self._addCountry(cur.right, countryToAdd)
            else:  # the right Country does not exist, so we can add this Country there
                cur.right = countryToAdd
        if countryToAdd.name == cur.name:  # special case where the population of the country being added is already within the tree
            print('Country already added to tree')

    def findPopulationFromCountry(self, name: str):
        print(f'Looking for population of country {name}.')
        if not self.root:
            print('   No tree exists')
        else:
            self._findPopulationFromCountry(self.root, name)
        return

    def _findPopulationFromCountry(self, cur: Country, name: str):
        if name > cur.name:
            if cur.right:
                self._findPopulationFromCountry(cur.right, name)
            else:
                print(f'   Country {name} does not exist in tree.')
                return
        elif name < cur.name:
            if cur.left:
                self._findPopulationFromCountry(cur.left, name)
            else:
                print(f'   Country {name} does not exist in tree.')
                return
        elif name == cur.name:
            print(f'   The population is {cur.population}')
            return

    def printLargestToSmallest(self, cur: Country, countryList=[]):
        if cur.left:
            self.printLargestToSmallest(cur.left, countryList)
        print(f'{cur}: {cur.population}')
        countryList.append(cur.name)
        if cur.right:
            self.printLargestToSmallest(cur.right, countryList)
        return countryList

    def __str__(self):
        self.printLargestToSmallest(self.root, [])
        return ''


class BST_Controller(object):
    def __init__(self):  # Constructor
        self.bst_c = CountryBST()
        self.bst_p = PopulationBST()


    def addCountry(self, countryToAdd: Country):
        self.bst_c.addCountry(countryToAdd)
        self.bst_p.addCountry(countryToAdd)


    def findCountryFromPopulation(self, population: int):
        self.bst_p.findCountryFromPopulation(population)


    def findPopulationFromCountry(self, name: str):
        self.bst_c.findPopulationFromCountry(name)


    def printByPopulation(self):
        print(self.bst_p)

    def printByCountry(self):
        print(self.bst_c)
        return


    def getCountryList(self):
        if not self.bst_c.root:
            return ['No Countries In Database']
        else:
            return self.bst_c.printLargestToSmallest(self.bst_c.root, [])

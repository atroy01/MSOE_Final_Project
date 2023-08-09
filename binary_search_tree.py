# Binary Search Tree classes for Project 10
# Andrew Troy
# 2023-08-09

class Country(object):  # One part of the data Tree
    def __init__(self, population: int, name: str, other_data=[]):  # Constructor
        self.population = population  # the population of the country. This is the key for the BST
        self.name = name
        self.other_data = other_data

class Node(object):  # One part of the data Tree
    def __init__(self, population: int, countries=[]):  # Constructor
        self.population = population  # the population of the country. This is the key for the BST
        self.left = None  # the left child
        self.right = None  # the right child
        self.countries = countries

    def __str__(self):
        country_names = ', '.join(country.name for country in self.countries)
        return f'{self.population}: {country_names}'

class CountryBST(object):  # A binary search tree of data elements
    def __init__(self):  # Constructor
        self.__root = None  # Reference to start of BST
        self.size = 0  # variable to keep track of the size of the tree

    def addCountry(self, country: Country):  # this is the starter form to check if the roo exists
        self.size += 1
        if not self.__root:
            self.__root = Node(country.population, [country])  # if no root exists, then create a new node with one country in it
        else:
            self._addCountry(self.__root, country)
        return

    def _addCountry(self, cur: Node, countryToAdd: Country):  # this is the recursive form of the function
        if countryToAdd.population < cur.population:
            if cur.left:
                self._addCountry(cur.left, countryToAdd)
            else:  # the left node does not exist, so we can add this node there
                cur.left = Node(countryToAdd.population, [countryToAdd])  # if no root exists, then create a new node with one country in it
        if countryToAdd.population > cur.population:
            if cur.right:
                self._addCountry(cur.right, countryToAdd)
            else:  # the right node does not exist, so we can add this node there
                cur.right = Node(countryToAdd.population, [countryToAdd])  # if no root exists, then create a new node with one country in it
        if countryToAdd.population == cur.population:  # special case where the population of the country being added is already within the tree
            cur.countries.append(countryToAdd)  # append the country to the countries list

    def findCountryFromPopulation(self, population: int):
        print(f'Looking for country with population of {population}.')
        if not self.__root:
            print('No tree exists')
        else:
            self._findCountryFromPopulation(self.__root, population, None, None)
        return

    def _findCountryFromPopulation(self, cur: Node, population: int, lastLeft: Node, lastRight: Node,):
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
        self.printLargestToSmallest(self.__root)
        return ''
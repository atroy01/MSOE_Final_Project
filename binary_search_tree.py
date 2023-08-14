# Binary Search Tree classes for Project 10
# Andrew Troy
# 2023-08-09
import main

class Country(object):  # One part of the data Tree
    def __init__(self, population: int, name: str, other_data=[]):  # Constructor
        self.population = population  # the population of the country. This is the key for the BST
        self.name = name.lower()
        self.enteredName = name  # use this for storing the name as it was entered. Helps to preserve capitalization.
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
        country_names = ', '.join(country.enteredName for country in self.countries)
        return f'{self.population:,} - {country_names}'


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
            return ['No countries to search from.', None]
        else:
            return self._findCountryFromPopulation(self.root, population, None, None)

    def _findCountryFromPopulation(self, cur: PopulationNode, population: int, lastLeft: PopulationNode, lastRight: PopulationNode,):
        countriesNames = []
        if population > cur.population:
            if cur.right:
                return self._findCountryFromPopulation(cur.right, population, lastLeft, cur)
            else:
                lastRight = cur
                ans = f'No exact match.\nNext smallest country: {lastRight}.\nNext largest country: {lastLeft}'
                print(ans)
                if lastRight: countriesNames.extend(lastRight.countries)
                if lastLeft: countriesNames.extend(lastLeft.countries)
                return [ans, countriesNames]
        elif population < cur.population:
            if cur.left:
                return self._findCountryFromPopulation(cur.left, population, cur, lastRight)
            else:
                lastLeft = cur
                ans = f'No exact match.\nNext smallest country: {lastRight}.\nNext largest country: {lastLeft}'
                print(ans)
                if lastRight: countriesNames.extend(lastRight.countries)
                if lastLeft: countriesNames.extend(lastLeft.countries)
                return [ans, countriesNames]
        elif population == cur.population:
            ans = f'Exact match: {cur}'
            countriesNames = cur.countries
            print(ans)
            return [ans, countriesNames]


    def findCountriesWithinRange(self, low: int, high: int):
        countries = []  # initialize a countries variable
        try:
            low = int(low)
            high = int(high)
            cur = self.root
            cur.left
            cur.right
            countries = self._findCountriesWithinRange(cur, low, high, countries)  # do a full search of the tree adding any countries that meet the criteria to the list
        except ValueError:
            countries = f'Invalid entry.'
        except AttributeError:  # I assume this is what gets thrown if self.root fails?
            countries = f'No countries in database.'
        print(countries)
        return countries

    def _findCountriesWithinRange(self, cur: PopulationNode, low: int, high: int, countries: []):
        if cur.left:
            countries = self._findCountriesWithinRange(cur.left, low, high, countries)
        if cur.right:
            countries = self._findCountriesWithinRange(cur.right, low, high, countries)
        if ((cur.population >= low) and (cur.population <= high)):
            countries.extend(cur.countries)
            return countries
        return countries



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

    def addCountry(self, country: Country):  # this is the starter form to check if the root exists
        self.size += 1
        if not self.root:
            self.root = country  # if no root exists, then make the passed country the root
            # self.addToCSV(country)
        else:
            self._addCountry(self.root, country)  # enter the recursive function
        return

    def _addCountry(self, cur: Country, countryToAdd: Country):  # this is the recursive form of the function
        if countryToAdd.name < cur.name:
            if cur.left:
                self._addCountry(cur.left, countryToAdd)
            else:  # the left Country does not exist, so we can add this Country there
                cur.left = countryToAdd
                # self.addToCSV(countryToAdd)
        if countryToAdd.name > cur.name:
            if cur.right:
                self._addCountry(cur.right, countryToAdd)
            else:  # the right Country does not exist, so we can add this Country there
                cur.right = countryToAdd
                # self.addToCSV(countryToAdd)
        if countryToAdd.name == cur.name:  # special case where the population of the country being added is already within the tree
            print('Country already added to database')


    def addToCSV(self, countryToAdd: Country):
        main.addCountryToCSV(countryToAdd)

    def findPopulationFromCountry(self, name: str):
        print(f'Looking for population of country {name}.')
        if not self.root:
            print('No database exists')
            return 'No countries in database.'
        else:
            return self._findPopulationFromCountry(self.root, name)

    def _findPopulationFromCountry(self, cur: Country, name: str):
        if name > cur.name:
            if cur.right:
                return self._findPopulationFromCountry(cur.right, name)
            else:
                ans = f'Country {name} does not exist database.'
                print(ans)
                return ans
        elif name < cur.name:
            if cur.left:
                return self._findPopulationFromCountry(cur.left, name)
            else:
                ans = f'Country {name} does not exist in database.'
                print(ans)
                return ans
        elif name == cur.name:
            ans = f'The population is {cur.population:,}'
            print(ans)
            return ans

    def printLargestToSmallest(self, cur: Country, countryList=[]):
        if cur.left:
            self.printLargestToSmallest(cur.left, countryList)
        print(f'{cur}: {cur.population}')
        countryList.append(cur.enteredName)
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
            return []
        else:
            return self.bst_c.printLargestToSmallest(self.bst_c.root, [])

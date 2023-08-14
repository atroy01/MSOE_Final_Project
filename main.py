# main.py for Final MSOE Python Course
# Andrew Troy
# 2023-08-08
import pandas as pd
from binary_search_tree import Country, PopulationNode, PopulationBST, CountryBST, BST_Controller
import csv

def main():
    # bst = testBST()
    # print(bst.findPopulationFromCountry('Tuvalu'))
    # bst = loadAllCountries(BST_Controller())
    # bst.printByCountry()
    # print(bst.bst_c.size)
    bst = createAndloadAllCountries()
    bst.printByCountry()

    pass

def createBST():
    return BST_Controller()


def addCountryFromDF(row, bst: BST_Controller):
    return bst.addCountry(Country(row['pop2023'],row['country'],[]))


def createAndloadAllCountries():
    bst = BST_Controller()
    csv_file_path = 'countries-table.csv'
    pop_data = pd.read_csv(csv_file_path)
    pop_data.apply(addCountryFromDF, axis=1, args=(bst,))
    return bst


def addCountryToCSV(countryToAdd: Country):
    # Data to be appended
    new_data = [countryToAdd.name, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', countryToAdd.population, '', '']
    # CSV file path
    csv_file_path = 'countries-table.csv'
    print('adding to csv')
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write the new data to the CSV file
        writer.writerow(new_data)


def testBST():
    bst = BST_Controller()  # create the BST
    bst.findPopulationFromCountry('England')
    bst.addCountry(Country(55, 'England', 'other data'))
    bst.addCountry(Country(300, 'USA', 'other data'))
    bst.addCountry(Country(1500, 'India', 'other data'))
    bst.addCountry(Country(2, 'Vatican City', 'other data'))
    bst.addCountry(Country(2, 'Tuvalu', 'other data'))
    bst.addCountry(Country(1497, 'China', 'other data'))
    print(bst)  # prints the tree largest to smallest followed by a blank line

    # Test find by country name
    bst.findPopulationFromCountry('Tuvalu')
    bst.findPopulationFromCountry('India')
    bst.findPopulationFromCountry('USA')

    # Test find by population number
    bst.findCountryFromPopulation(56)
    bst.findCountryFromPopulation(150)
    bst.findCountryFromPopulation(151)
    bst.findCountryFromPopulation(152)
    bst.findCountryFromPopulation(300)
    bst.findCountryFromPopulation(301)
    bst.findCountryFromPopulation(1499)
    print(f'Number of Countries in Tree: {bst.bst_c.size}')
    return bst

if __name__ == "__main__":
    main()

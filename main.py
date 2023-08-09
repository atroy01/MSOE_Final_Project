# main.py for Final MSOE Python Course
# Andrew Troy
# 2023-08-08


import pandas as pd
from binary_search_tree import Country, Node, CountryBST


def main():
    mybst = CountryBST()
    mybst.findCountryFromPopulation(45)


    mybst.addCountry(Country(55,'England', 'other data'))
    mybst.addCountry(Country(300, 'USA', 'other data'))
    mybst.addCountry(Country(1500, 'India', 'other data'))
    mybst.addCountry(Country(2, 'Vatican City', 'other data'))
    mybst.addCountry(Country(2, 'Tuvalu', 'other data'))
    mybst.addCountry(Country(1497, 'China', 'other data'))
    print(mybst)  # prints the tree largest to smallest followed by a blank line

    mybst.findCountryFromPopulation(56)
    mybst.findCountryFromPopulation(150)
    mybst.findCountryFromPopulation(151)
    mybst.findCountryFromPopulation(152)
    mybst.findCountryFromPopulation(300)
    mybst.findCountryFromPopulation(301)
    mybst.findCountryFromPopulation(1499)


    print(f'Number of Countries in Tree: {mybst.size}')
    print('debug')

# csv_file_path = 'countries-table.csv'
# # Read the Population Data from the CSV file into a DataFrame
# pop_data = pd.read_csv(csv_file_path)




# # Specify the column in which you want to check for duplicate values
# column_to_check = 'pop2023'  # Replace 'column_name' with the actual column name
#
# # Check for duplicate values in the specified column
# duplicates = df[df.duplicated(subset=column_to_check, keep=False)]
#
# if not duplicates.empty:
#     print("Duplicate values found in the column:")
#     print(duplicates)
# else:
#     print("No duplicate values found in the column.")


if __name__ == "__main__":
    main()

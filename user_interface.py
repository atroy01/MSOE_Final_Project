import tkinter as tk
from tkinter import font
from tkinter import messagebox
import main
from binary_search_tree import BST_Controller, Country
from entryWithPlaceholder import EntryWithPlaceholder

class ApplicationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Country and Population Dashboard")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="darkgrey")  # Use the color you want
        self.bst = BST_Controller()

        # Add Title
        my_font = font.Font(family='Helvetica', size=30)
        self.titleText = tk.Label(self.root, text='Country and Population Dashboard', bg="lightgrey", font=my_font)
        self.titleText.place(x=150, y=10)

        # PLACE METHOD
        # Add All Countries button
        button_addAllCountries = tk.Button(root, text="Add All 234 Countries To Database",
                                           command=self.addAllCountries,
                                           padx=25, pady=10, bg="lightgrey", width=20)
        button_addAllCountries.place(x=10, y=85, anchor='nw')
        button_clearAllCountries = tk.Button(root, text="Clear Database",
                                           command=self.clearAllCountries,
                                           padx=25, pady=10, bg="lightgrey", width=15)
        button_clearAllCountries.place(x=225, y=85, anchor='nw')

        # Add Find Countries button and entry
        self.entry_findCountry = EntryWithPlaceholder(root, 'Enter Population #')
        self.entry_findCountry.place(x=10, y=150, anchor='nw')
        self.button_findCountry = tk.Button(root, text="Find Country From Population",
                                           command=self.findCountry,
                                           padx=25, pady=10, bg="lightgrey", width=25)
        self.button_findCountry.place(x=150, y=150, anchor='nw')
        self.findCountryOutput = tk.Label(self.root, text='-', wraplength=260, justify='left')
        self.findCountryOutput.place(x=400, y=150, anchor='nw')

        # Add Find Population button and entry
        self.entry_findPopulation = EntryWithPlaceholder(root, 'Enter Country name')
        self.entry_findPopulation.place(x=10, y=250, anchor='nw')
        self.button_findPopulation = tk.Button(root, text="Find Population From Country Name",
                                           command=self.findPopulation,
                                           padx=25, pady=10, bg="lightgrey", width=25)
        self.button_findPopulation.place(x=150, y=250, anchor='nw')
        self.findPopulationOutput = tk.Label(self.root, text='-', wraplength=260, justify='left')
        self.findPopulationOutput.place(x=400, y=250, anchor='nw')

        # Add Add New Country fields
        self.entry_addCountry = EntryWithPlaceholder(root, 'Enter Country Name')
        self.entry_addCountry.place(x=10, y=350, anchor='nw')
        self.entry_addPopulation = EntryWithPlaceholder(root, 'Enter Population #')
        self.entry_addPopulation.place(x=10, y=370, anchor='nw')
        self.button_addCountry = tk.Button(root, text="Add Country To Database",
                                               command=self.addCountry,
                                               padx=25, pady=10, bg="lightgrey", width=25)
        self.button_addCountry.place(x=150, y=350, anchor='nw')
        self.addCountryOutput = tk.Label(self.root, text='-', wraplength=250, justify='left')
        self.addCountryOutput.place(x=400, y=350, anchor='nw')


        # Find Countries in Range
        self.entry_lowRange = EntryWithPlaceholder(root, 'Enter Low Range')
        self.entry_lowRange.place(x=10, y=450, anchor='nw')
        self.entry_highRange = EntryWithPlaceholder(root, 'Enter High Range')
        self.entry_highRange.place(x=10, y=470, anchor='nw')
        self.button_withinRange = tk.Button(root, text="Find Countries within Population Range",
                                           command=self.findCountriesWithinRange,
                                           padx=25, pady=10, bg="lightgrey", width=25)
        self.button_withinRange.place(x=150, y=450, anchor='nw')
        self.rangeOutput = tk.Label(self.root, text='-', wraplength=260, justify='left')
        self.rangeOutput.place(x=400, y=450, anchor='nw')


        # Create a list box with the countries
        self.listbox = tk.Listbox(self.root)
        self.listbox.place(x=670, y=102, anchor='nw')
        self.listbox.config(height=30, width=35)
        self.listboxlabel = tk.Label(self.root,text='Database',bg='lightgrey')
        self.listboxlabel.place(x=670, y=75, anchor='nw')


    def highlight_country(self, country_to_highlight: str):
        for index in range(self.listbox.size()):
            item_text = self.listbox.get(index)
            if country_to_highlight.lower() == item_text.lower():  # Case-insensitive match
                self.listbox.itemconfig(index, {'bg': 'yellow'})

    def clear_highlighting(self):
        for index in range(self.listbox.size()):
            self.listbox.itemconfig(index, {'bg': 'white'})

    def updateListBox(self):
        self.listbox.delete(0,tk.END)
        countries = self.bst.getCountryList()
        for country in countries:
            self.listbox.insert(tk.END, country)

    def addAllCountries(self):
        self.bst = main.createAndloadAllCountries()
        self.bst.printByCountry()
        self.updateListBox()

    def clearAllCountries(self):
        self.bst.bst_p.root = None
        self.bst.bst_c.root = None
        self.updateListBox()

    def findCountry(self):
        self.clear_highlighting()
        population = self.entry_findCountry.get()
        ansList = []
        try:
            population = int(population)
            ansList = self.bst.bst_p.findCountryFromPopulation(int(population))
            if ansList[1]:
                for country in ansList[1]:
                    self.highlight_country(country.name)
        except ValueError:
            print('You need to enter a number')
            ansList.append('You need to enter a number')
        self.findCountryOutput.config(text=ansList[0])


    def findPopulation(self):
        self.clear_highlighting()
        country = self.entry_findPopulation.get()
        self.highlight_country(country)
        try:
            ans = self.bst.bst_c.findPopulationFromCountry(str(country).lower())
        except ValueError:
            print('You need to enter text')
            ans = 'You need to enter text'
        self.findPopulationOutput.config(text=ans)

    def addCountry(self):
        countryName = self.entry_addCountry.get()
        countryPop = self.entry_addPopulation.get()
        try:
            self.bst.addCountry(Country(int(countryPop),str(countryName)))
            ans = f'A country named {str(countryName)}, with population of {int(countryPop):,} added to list.'
            print('hello')
        except ValueError:
            ans = 'Country name must be text.\nCountry population must be a number.'
        self.addCountryOutput.config(text=ans)
        self.updateListBox()
        self.highlight_country(countryName)

    def findCountriesWithinRange(self):
        low = self.entry_lowRange.get()
        high = self.entry_highRange.get()
        countries = self.bst.bst_p.findCountriesWithinRange(low, high)
        self.clear_highlighting()
        #print(f'Countries in range: {[country.name for country in countries]}')
        if (isinstance(countries, list) and len(countries) > 0):
            for country in countries:
                print(f'Country: {country.enteredName} | Pop: {country.population:,}')
                self.highlight_country(country.name)
            self.rangeOutput.config(text='Countries within range are highlighted in database.')
        elif (isinstance(countries, list) and len(countries) == 0):
            print('No countries in database')
            self.rangeOutput.config(text='No countries in database.')
        else:
            print('Invalid Entry')
            self.rangeOutput.config(text='Invalid Entry')


if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationGUI(root)
    root.mainloop()
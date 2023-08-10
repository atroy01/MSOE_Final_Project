import tkinter as tk
from tkinter import messagebox
import main
from binary_search_tree import BST_Controller
#
# def function1():
#     input_text = entry1.get()
#     main.main()
#     # Add your function logic here for field 1
#     messagebox.showinfo("Function 1 Result", f"Entered Text: {input_text}")
#
# def function2():
#     input_text = entry2.get()
#     # Add your function logic here for field 2
#     messagebox.showinfo("Function 2 Result", f"Entered Text: {input_text}")
#
# def function3():
#     input_text = entry3.get()
#     # Add your function logic here for field 3
#     messagebox.showinfo("Function 3 Result", f"Entered Text: {input_text}")

# # Create the main application window
# root = tk.Tk()
# root.title("Dashboard")


# add all countries

# Create text entry fields
# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)
# entry3 = tk.Entry(root)

# # Create buttons and associate functions
# button1 = tk.Button(root, text="Run Function 1", command=function1)
# button2 = tk.Button(root, text="Run Function 2", command=function2)
# button3 = tk.Button(root, text="Run Function 3", command=function3)

# # Layout using grid
# entry1.grid(row=0, column=0, padx=10, pady=5)
# entry2.grid(row=1, column=0, padx=10, pady=5)
# entry3.grid(row=2, column=0, padx=10, pady=5)
#
# button1.grid(row=0, column=1, padx=10, pady=5)
# button2.grid(row=1, column=1, padx=10, pady=5)
# button3.grid(row=2, column=1, padx=10, pady=5)
# button_addAllCountries.grid(row=3, column=1, padx=50, pady=50)

# # Start the GUI event loop
# root.mainloop()

class ApplicationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")  # Use the color you want
        self.bst = BST_Controller()

        # MASHED UP METHOD (ORIGINAL)
        # # Add All Countries button
        # button_addAllCountries = tk.Button(root, text="Add All Countries To Database",
        #                                    command=self.addAllCountries,
        #                                    padx=25, pady=10, bg="lightgreen")
        # button_addAllCountries.pack(padx=10, pady=10, anchor='w')
        #
        # # Get Bahamas Population button
        # button_findBahamas = tk.Button(root, text='Get Bahamas Population',
        #                                command=self.findBahamas,
        #                                padx=25, pady=10, bg="lightgreen")
        # button_findBahamas.pack(padx=10, pady=10, anchor='w')
        #
        # # Create List
        # countries = self.bst.getCountryList()
        # countryList = ', '.join(countries)
        # self.txt = tk.Text(self.root, wrap=tk.WORD, width=45, height = 30)
        # self.txt.insert(tk.END, countryList)
        # self.txt.place(x=400, y=10, anchor='nw')
        #
        # # Create a Scrollbar widget
        # scrollbar = tk.Scrollbar(root, command=self.txt.yview)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #
        # # Associate the Scrollbar with the Text widget
        # self.txt.config(yscrollcommand=scrollbar.set)
        #
        # # Create List
        # countries = self.bst.getCountryList()
        # countryList = ', '.join(countries)
        # self.txt = tk.Text(self.root, wrap=tk.WORD, width=45, height=30)
        # self.txt.insert(tk.END, countryList)
        #
        # # Create a Scrollbar widget
        # scrollbar = tk.Scrollbar(self.root, command=self.txt.yview)
        # scrollbar.grid(row=0, column=1, sticky=tk.NS)  # Place the scrollbar next to the Text widget
        #
        # self.txt.grid(row=0, column=0, sticky=tk.NSEW)  # Use NSEW to make Text widget expand with window
        #
        # # Configure row and column weights to make widgets expand properly
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)


        ## GRID METHOD
        # # Add All Countries button
        # button_addAllCountries = tk.Button(root, text="Add All Countries To Database",
        #                                    command=self.addAllCountries,
        #                                    padx=25, pady=10, bg="lightgreen")
        # button_addAllCountries.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        #
        # # Get Bahamas Population button
        # button_findBahamas = tk.Button(root, text='Get Bahamas Population',
        #                                command=self.findBahamas,
        #                                padx=25, pady=10, bg="lightgreen")
        # button_findBahamas.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        #
        # # Create List
        # countries = self.bst.getCountryList()
        # countryList = ', '.join(countries)
        # self.txt = tk.Text(self.root, wrap=tk.WORD, width=45, height=30)
        # self.txt.insert(tk.END, countryList)
        # self.txt.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nw')
        #
        # # Create a Scrollbar widget
        # scrollbar = tk.Scrollbar(root, command=self.txt.yview)
        # scrollbar.grid(row=0, column=2, rowspan=2, sticky='ns')
        #
        # # Associate the Scrollbar with the Text widget
        # self.txt.config(yscrollcommand=scrollbar.set)


        ### PACK METHOD
        # # Add All Countries button
        # button_addAllCountries = tk.Button(root, text="Add All Countries To Database",
        #                                    command=self.addAllCountries,
        #                                    padx=25, pady=10, bg="lightgreen")
        # button_addAllCountries.pack(anchor='w', padx=10, pady=10)
        #
        # # Get Bahamas Population button
        # button_findBahamas = tk.Button(root, text='Get Bahamas Population',
        #                                command=self.findBahamas,
        #                                padx=25, pady=10, bg="lightgreen")
        # button_findBahamas.pack(anchor='w', padx=10, pady=10)
        #
        # # Create List
        # countries = self.bst.getCountryList()
        # countryList = ', '.join(countries)
        # self.txt = tk.Text(self.root, wrap=tk.WORD, width=45, height=30)
        # self.txt.insert(tk.END, countryList)
        # self.txt.pack(side=tk.LEFT, padx=10, pady=10)
        #
        # # Create a Scrollbar widget
        # scrollbar = tk.Scrollbar(root, command=self.txt.yview)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #
        # # Associate the Scrollbar with the Text widget
        # self.txt.config(yscrollcommand=scrollbar.set)

        # PLACE METHOD
        # Add All Countries button
        button_addAllCountries = tk.Button(root, text="Add All Countries To Database",
                                           command=self.addAllCountries,
                                           padx=25, pady=10, bg="lightgreen")
        button_addAllCountries.place(x=10, y=35, anchor='w')

        # Get Bahamas Population button
        button_findBahamas = tk.Button(root, text='Get Bahamas Population',
                                       command=self.findBahamas,
                                       padx=25, pady=10, bg="lightgreen")
        button_findBahamas.place(x=10, y=100, anchor='w')

        # Create List
        countries = self.bst.getCountryList()
        countryList = ', '.join(countries)
        self.txt = tk.Text(root, wrap=tk.WORD, width=50, height=35)
        self.txt.insert(tk.END, countryList)
        self.txt.place(x=300, y=10, anchor='nw')

        # Create a Scrollbar widget
        scrollbar = tk.Scrollbar(root, command=self.txt.yview)
        scrollbar.place(x=702, y=10, anchor='nw', height=564)

        # Associate the Scrollbar with the Text widget
        self.txt.config(yscrollcommand=scrollbar.set)

    def updateList(self):
        countries = self.bst.getCountryList()
        countryList = ', '.join(countries)
        self.txt.delete(1.0, tk.END)  # Clear previous content
        self.txt.insert(tk.END, countryList)


        #
        # txt = tk.Text(self.root, fg='black', bg='lightgreen', relief=RAISED)
        # txt.insert(INSERT,)
        # countryList = tk.Label(self.root, wraplength=390, text=countryList)
        # countryList.place(x=400, y=10, anchor='nw')


    def addAllCountries(self):
        self.bst = main.createAndloadAllCountries()
        self.bst.printByCountry()
        self.updateList()


    def findBahamas(self):
        self.bst.findPopulationFromCountry('Bahamas')


if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationGUI(root)
    root.mainloop()
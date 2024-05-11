import tkinter as tk
from tkinter.ttk import Separator
from tkinter import CENTER, NORMAL, DISABLED, VERTICAL, IntVar, Label, Button, Entry, Checkbutton, StringVar, messagebox, Tk
from model import MathOperations, UiFunctions

class Gui(tk.Tk):
    def __init__(self, math_functions:MathOperations, ui_functions:UiFunctions) -> None: 
        super().__init__()
        self.math_functions = math_functions
        self.ui_functions = ui_functions
        self.permutations_checkbox_value = IntVar()
        self.combinations_checkbox_value = IntVar()
        self.repeat_checkbox_value = IntVar()
        self.n = IntVar()
        self.k = IntVar()
        self.result_string = StringVar()

        #Window set-up
        self.bind("<Escape>", lambda x : self.destroy())
        self.bind("<Return>", lambda x : ui_functions.validate_integer_input())
        self.geometry('')
        self.title('Combinatorics Generator')
        
        # self.icon = self.iconbitmap('Coding/Python/Combinatorics-Generator/safe.ico')
        self.separator_left = Separator(self, orient=VERTICAL)
        self.separator_right = Separator(self, orient=VERTICAL)

        #Labels
        self.permutation_label = Label(self, text='Permutations')
        self.combination_label = Label(self, text='Combinations')
        self.repeat_label = Label(self, text='Repeats allowed')
        self.result_label = Label(self, text='Results:', justify=CENTER)
        self.print_results = Label(self, textvariable=self.result_string, justify=CENTER,font='Verdana 9 bold')

        #Checkbuttons
        self.select_permutations = Checkbutton(self, 
                                               variable=self.permutations_checkbox_value, 
                                               onvalue=1, 
                                               offvalue=0, 
                                               command=self.disable_combination_checkbox
                                               )
        self.select_combinations = Checkbutton(self, 
                                               variable=self.combinations_checkbox_value, 
                                               onvalue=1, 
                                               offvalue=0, 
                                               command=self.disable_permutation_checkbox
                                               )
        self.select_repeats = Checkbutton(self, 
                                          variable=self.repeat_checkbox_value, 
                                          onvalue=1, 
                                          offvalue=0
                                          )

        #Labels
        self.n_label = Label(self, text='Enter n:')
        self.k_label = Label(self, text='Enter k:')

        #Entries
        self.n_entry = Entry(self, textvariable=self.n, width=10, justify='center')
        self.k_entry = Entry(self, textvariable=self.k, width=10, justify='center')

        #Button
        self.calc = Button(self, text='Calculate', command=ui_functions.validate_integer_input)

        #Grid left
        self.permutation_label.grid(row=0, column=0, pady=5)
        self.combination_label.grid(row=2, column=0, pady=5)
        self.repeat_label.grid(row=4, column=0, pady=2.5)
        self.select_permutations.grid(row=1, column=0)
        self.select_combinations.grid(row=3, column=0)
        self.select_repeats.grid(row=5, column=0, pady=2.5)
        self.separator_left.grid(row=0, column=1, rowspan=6, sticky='ns', padx=5, pady=5)
        
        #Grid Center
        self.n_label.grid(row=0, column=2)
        self.k_label.grid(row=2, column=2)
        self.n_entry.grid(row=1, column=2, padx=10, pady=2)
        self.k_entry.grid(row=3, column=2, padx=10, pady=2)
        self.calc.grid(row=4, column=2, rowspan=2)
        self.separator_right.grid(row=0, column=3, rowspan=6, sticky='ns', padx=5, pady=5)
        
        #Grid Right
        self.result_label.grid(row=0, column=4, columnspan=6)
        self.print_results.grid(row=2, column=4, rowspan=2)

    #Updates result_string
    def update_result_label(self) -> None:
        """Updates the result_string variable based on user inputs"""
        self.print_results.config(text='', padx=5)
        self.print_results.config(text=self.result_string.get())

    #Checkbutton functions
    def disable_combination_checkbox(self) -> None:
        """Disables combination checkbutton if permutations checkbutton is active"""
        if self.permutations_checkbox_value.get() == 1:
            self.select_combinations.config(state=DISABLED)
        else:
            self.select_combinations.config(state=NORMAL)

    def disable_permutation_checkbox(self) -> None:
        """Disables permutations checkbutton if combination checkbutton is active"""
        if self.combinations_checkbox_value.get() == 1:
            self.select_permutations.config(state=DISABLED)
        else:
            self.select_permutations.config(state=NORMAL)
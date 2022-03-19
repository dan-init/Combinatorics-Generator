from math import factorial
from tkinter import CENTER, NORMAL, DISABLED, VERTICAL, IntVar, Label, Button, Entry, Checkbutton, StringVar, messagebox, Tk
from tkinter.ttk import Separator

root = Tk()
permutations_checkbox_value = IntVar()
combinations_checkbox_value = IntVar()
repeat_checkbox_value = IntVar()
n = IntVar()
k = IntVar()
result_string = StringVar()

#Error Handling
def validate_integer_input():
    """Displays error message if integer is not entered in either entries"""
    while True:
        try:
            n.get() or k.get() == int
        except Exception as e0:
            e0 = 'n and k must be an integer'
            return messagebox.showerror('User Error', e0)
        else:
            validate_positive_integer()
            break

def validate_positive_integer():
    while True:
        if n.get() <=0 or k.get() <=0:
            return messagebox.showerror('User error', 'Integer must be greater than 0')
        else:
            display_results()
            break

def selection_error_message():
    """Displays error message if permutations or combinatons checkbuttons state is not active"""
    if permutations_checkbox_value.get() == 0 and combinations_checkbox_value.get() == 0 and repeat_checkbox_value.get() == 0 or 1:
        messagebox.showerror('User Error', 'Please select Combinations or Permutations!')

#User Prompts
def display_results():
    """Displays messagebox depending on which checkboxes are selected"""
    if permutations_checkbox_value.get() == 1 and repeat_checkbox_value.get() == 0:
        permutations_no_repeats(n, k)
    elif permutations_checkbox_value.get() == 1 and repeat_checkbox_value.get() == 1:
        permutations_with_repeats(n, k)
    elif combinations_checkbox_value.get() == 1 and repeat_checkbox_value.get() == 0:
        combinations_no_repeats(n, k)
    elif combinations_checkbox_value.get() == 1 and repeat_checkbox_value.get() == 1:
        combinations_with_repeats(n,k)
    else:
        selection_error_message()
    
#Mathmatical operations
def permutations_no_repeats(n:int, k:int) -> int:
    """Returns number of permutations possible where numbers cannot repeat"""
    non_repeat_permutations = (factorial(n.get())//factorial(n.get()-k.get()))
    result_string.set('Permutations without\nrepeat numbers:\n\n'+ str("{:,}".format(non_repeat_permutations)))
    #Callback to functions inside Gui class
    UI = Gui(primary=root)
    UI.update_result_label()
    UI.disable_combination_checkbox()

def permutations_with_repeats(n:int, k:int) -> int:
    """Returns number of permutations possible where numbers can repeat"""
    repeat_permutations = (n.get()**k.get())
    result_string.set('Permutations with\nrepeat numbers:\n\n'+ str("{:,}".format(repeat_permutations)))
    #Callback to functions inside Gui class
    UI = Gui(primary=root)
    UI.update_result_label()
    UI.disable_combination_checkbox()

def combinations_no_repeats(n:int, k:int) -> int:
    """Returns number of possible combinations where numbers cannot repeat"""
    non_repeat_combinations = (factorial(n.get())//(factorial(k.get())*factorial(n.get()-k.get())))
    result_string.set('Combinations without\nrepeat numbers:\n\n'+ str("{:,}".format(non_repeat_combinations)))
    #Callback to functions inside Gui class
    UI = Gui(primary=root)
    UI.update_result_label()
    UI.disable_permutation_checkbox()

def combinations_with_repeats(n:int, k:int) -> int:
    """Returns number of possible combitions where numbers can repeat"""
    repeat_combinations = factorial(k.get() + (n.get()-1))//(factorial(k.get())*(factorial(n.get()-1)))
    result_string.set('Combintations with\nrepeat numbers:\n\n' + str("{:,}".format(repeat_combinations)))
    #Callback to functions inside Gui class
    UI = Gui(primary=root)
    UI.update_result_label()
    UI.disable_permutation_checkbox()

class Gui:
    def __init__(self, primary): 
        
        #Window set-up
        self.primary = self
        primary.bind("<Escape>", lambda x : root.destroy())
        primary.geometry('')
        self.title = root.title('Combinatorics Generator')
        self.icon = root.iconbitmap('C:/Users/ab5302/Documents/GitHub/Combinatorics-Generator/safe.ico')
        self.separator_left = Separator(root, orient=VERTICAL)
        self.separator_right = Separator(root, orient=VERTICAL)

        #Labels
        self.permutation_label = Label(root, text='Permutations')
        self.combination_label = Label(root, text='Combinations')
        self.repeat_label = Label(root, text='Repeats allowed')
        self.result_label = Label(root, text='Results:')
        self.print_results = Label(root, textvariable=result_string, justify=CENTER,font='Verdana 9 bold')

        #Checkbuttons
        self.select_permutations = Checkbutton(root, variable=permutations_checkbox_value, onvalue=1, offvalue=0, command=self.disable_combination_checkbox)
        self.select_combinations = Checkbutton(root, variable=combinations_checkbox_value, onvalue=1, offvalue=0, command=self.disable_permutation_checkbox)
        self.select_repeats = Checkbutton(root, variable=repeat_checkbox_value, onvalue=1, offvalue=0)

        #Labels
        self.n_label = Label(root, text='Enter n:')
        self.k_label = Label(root, text='Enter k:')

        #Entries
        self.n_entry = Entry(root, textvariable=n, width=10, justify='center')
        self.k_entry = Entry(root, textvariable=k, width=10, justify='center')

        #Button
        self.calc = Button(root, text='Calculate', command=validate_integer_input)

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
        self.result_label.grid(row=0, column=4)
        self.print_results.grid(row=2, column=4, rowspan=2)

    #Updates results_
    def update_result_label(self):
        """Updates the result_string variable based on user inputs"""
        self.print_results.config(text='')
        self.print_results.config(text=result_string.get())

    #Checkbutton functions
    def disable_combination_checkbox(self):
        """Disables combination checkbutton if permutations checkbutton is active"""
        if permutations_checkbox_value.get() == 1:
            self.select_combinations.config(state=DISABLED)
        else:
            self.select_combinations.config(state=NORMAL)

    def disable_permutation_checkbox(self):
        """Disables permutations checkbutton if combination checkbutton is active"""
        if combinations_checkbox_value.get() == 1:
            self.select_permutations.config(state=DISABLED)
        else:
            self.select_permutations.config(state=NORMAL)

def main():
    Gui(root)
    root.mainloop()

main()
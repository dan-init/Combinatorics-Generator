from math import factorial
from tkinter import VERTICAL, IntVar, Label, Button, Entry, Checkbutton, messagebox, Tk
from tkinter import NORMAL, DISABLED, VERTICAL, IntVar, Label, Button, Entry, Checkbutton, messagebox, Tk
from tkinter.ttk import Separator

root = Tk()
permutations_checkbox_value = IntVar()
combinations_checkbox_value = IntVar()
repeat_checkbox_value = IntVar()
n = IntVar()
k = IntVar()

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
        display_error_message()
        display_integer_error()

def display_error_message():
    """Displays error message if prerequesite conidtions are not met"""
    if permutations_checkbox_value.get() == 0 and combinations_checkbox_value.get() == 0 and repeat_checkbox_value.get() == 0 or 1:
        messagebox.showerror('Error', 'Please select Combinations or Permutations!')

def display_integer_error():
    """Displays error message if integer is not entered in either entries"""
    if n.get() or k.get() == type(''):
        return messagebox.showerror('Error', 'Input should be integer')

#Mathmatical operations
def permutations_no_repeats(n:int, k:int) -> int:
    """Returns number of permutations possible where numbers cannot repeat"""
    non_repeat_permutations = (factorial(n.get())//factorial(n.get()-k.get()))
    
    return messagebox.showinfo('Permutation Results', 
    'Permutations without repeat numbers: '+ str("{:,}".format(non_repeat_permutations))) 
    
def permutations_with_repeats(n:int, k:int) -> int:
    """Returns number of permutations possible where numbers can repeat"""
    repeat_permutations = (n.get()**k.get())
    
    return messagebox.showinfo('Permutations Results',
    'Permutations with repeat numbers: '+ str("{:,}".format(repeat_permutations)))

def combinations_no_repeats(n:int, k:int) -> int:
    """Returns number of possible combinations where numbers cannot repeat"""
    non_repeat_combinations = (factorial(n.get())//(factorial(k.get())*factorial(n.get()-k.get())))
    
    return messagebox.showinfo('Combination Results', 
    'Combinations without repeat numbers: '+ str("{:,}".format(non_repeat_combinations)))
   
def combinations_with_repeats(n:int, k:int) -> int:
    """Returns number of possible combitions where numbers can repeat"""
    repeat_combinations = factorial(k.get() + (n.get()-1))//(factorial(k.get())*(factorial(n.get()-1)))
    
    return messagebox.showinfo('Combination Results', 
    'Combintations with repeat numbers: ' + str("{:,}".format(repeat_combinations)))

class Gui:
    def __init__(self, master): 

        #Window set-up
        self.master = self
        master.bind("<Escape>", lambda x : root.destroy())
        self.title = root.title('Combinatorics Generator')
        self.icon = root.iconbitmap('C:/Users/ab5302/Documents/GitHub/Combinatorics-Generator/safe.ico')
        self.separator = Separator(root, orient = VERTICAL)

        #Labels
        self.permutation_label = Label(root, text='Permutations')
        self.combination_label = Label(root, text='Combinations')
        self.repeat_label = Label(root, text='Repeats allowed')

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
        self.calc = Button(root, text='Calculate', command=display_results)

        #Grid
        self.n_label.grid(row=0, column=2)
        self.k_label.grid(row=2, column=2)
        self.n_entry.grid(row=1, column=2, padx=10, pady=2)
        self.k_entry.grid(row=3, column=2, padx=10, pady=2)
        self.calc.grid(row=4, column=2, rowspan=2)
        self.separator.grid(row=0, column=1, rowspan=6, sticky='ns', padx=5, pady=5)
        self.permutation_label.grid(row=0, column=0)
        self.combination_label.grid(row=2, column=0)
        self.repeat_label.grid(row=4, column=0)
        self.select_permutations.grid(row=1, column=0)
        self.select_combinations.grid(row=3, column=0)
        self.select_repeats.grid(row=5, column=0)

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
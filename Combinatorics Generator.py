from math import factorial
from tkinter import IntVar, Label, Button, Entry, Checkbutton, messagebox, Tk

root = Tk()
permutations_checkbox_state = IntVar()
combinations_checkbox_state = IntVar()
n = IntVar()
k = IntVar()

def display_results():
        if permutations_checkbox_state.get() == 1:
            permutations(n, k)
        elif combinations_checkbox_state.get() ==1:
            combinations(n, k)

def permutations(n:int, k:int) -> int:
    """Function to return the number of permutations for two given integers"""
    non_repeat_permutations = (factorial(n.get())//factorial(n.get()-k.get()))
    repeat_permutations = (n.get()**k.get())

    return messagebox.showinfo('Permutation Results', 
    'Permutations without repeat numbers: '+ str("{:,}".format(non_repeat_permutations)) + 
    '\nPermutations with repeat numbers: '+ str("{:,}".format(repeat_permutations)))

def combinations(n:int, k:int) -> int:
    """Function which returns the number of combinations possible from two given integers"""
    non_repeat_combinations = (factorial(n.get())//(factorial(k.get())*factorial(n.get()-k.get())))
    repeat_combinations = factorial(k.get() + (n.get()-1))//(factorial(k.get())*(factorial(n.get()-1)))

    return messagebox.showinfo('Combination Results', 
    'Combinations without repeat numbers: '+ str("{:,}".format(non_repeat_combinations)) + 
    '\nCombinations with repeat numbers: '+ str("{:,}".format(repeat_combinations)))

class Gui:
    def __init__(self, master):
        
        #Window set-up
        self.master = master
        master.bind("<Escape>", lambda x : root.destroy())
        master.title = root.title('Combinatorics Generator')
        master.icon = root.iconbitmap('C:/Users/ab5302/Documents/GitHub/Combinatorics-Generator/safe.ico')

        #Labels
        master.permutation_label = Label(root, text='Permutations')
        master.combination_label = Label(root, text='Combinations')

        #Checkbutton
        master.select_permutations = Checkbutton(root, variable=permutations_checkbox_state, onvalue=1, offvalue=0 )
        master.select_combinations = Checkbutton(root, variable=combinations_checkbox_state, onvalue=1, offvalue=0)

        #Labels
        master.n_label = Label(root, text='Enter n:')
        master.k_label = Label(root, text='Enter k:')

        #Entries
        master.n_entry = Entry(root, textvariable=n)
        master.k_entry = Entry(root, textvariable=k)

        #Button
        master.calc = Button(root, text='Calculate', command=display_results)

        #Grid
        master.permutation_label.grid(row=0, column=0)
        master.combination_label.grid(row=0, column=1)
        master.select_permutations.grid(row=1, column=0)
        master.select_combinations.grid(row=1, column=1)
        master.n_label.grid(row=2, column=0)
        master.k_label.grid(row=2, column=1)
        master.n_entry.grid(row=3, column=0, padx=5, pady=5)
        master.k_entry.grid(row=3, column=1, padx=5, pady=5)
        master.calc.grid(row=4, columnspan=2, pady=5)

def main():
    Gui(root)
    root.mainloop()

main()
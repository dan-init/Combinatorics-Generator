from math import factorial
from tkinter import IntVar, Label, Button, Entry, Checkbutton, messagebox, Tk

root = Tk()
permutations_checkbox_state = IntVar()
combinations_checkbox_state = IntVar()
repeat_checkbox_state = IntVar()
n = IntVar()
k = IntVar()

def display_results():
    """Displays messagebox depending on which checkbox is selected"""
    if permutations_checkbox_state.get() == 1 and repeat_checkbox_state.get() == 0:
        permutations_no_repeats(n, k)
    elif permutations_checkbox_state.get() == 1 and repeat_checkbox_state.get() == 1:
        permutations_with_repeats(n, k)
    elif combinations_checkbox_state.get() == 1 and repeat_checkbox_state.get() ==0:
        combinations_no_repeats(n, k)
    elif combinations_checkbox_state.get() == 1 and repeat_checkbox_state.get() == 1:
        combinations_with_repeats(n,k)

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
    """Function which returns the number of combinations possible from two given integers"""
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
        self.master = master
        master.bind("<Escape>", lambda x : root.destroy())
        master.title = root.title('Combinatorics Generator')
        master.icon = root.iconbitmap('C:/Users/ab5302/Documents/GitHub/Combinatorics-Generator/safe.ico')

        #Labels
        master.permutation_label = Label(root, text='Permutations')
        master.combination_label = Label(root, text='Combinations')
        master.repeat_label = Label(root, text='Repeats allowed')
        master.space_label = Label(root, text=' ')

        #Checkbuttons
        master.select_permutations = Checkbutton(root, variable=permutations_checkbox_state, onvalue=1, offvalue=0 )
        master.select_combinations = Checkbutton(root, variable=combinations_checkbox_state, onvalue=1, offvalue=0)
        master.select_repeats = Checkbutton(root, variable=repeat_checkbox_state, onvalue=1, offvalue=0)

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
        master.repeat_label.grid(row=0, column=2)
        master.select_permutations.grid(row=1, column=0)
        master.select_combinations.grid(row=1, column=1)
        master.select_repeats.grid(row=1, column= 2)
        master.space_label.grid(row=2, columnspan=3)
        master.n_label.grid(row=3, column=0)
        master.k_label.grid(row=3, column=1)
        master.n_entry.grid(row=4, column=0, padx=5, pady=5)
        master.k_entry.grid(row=4, column=1, padx=5, pady=5)
        master.calc.grid(row=4, column=2, pady=5)

def main():
    Gui(root)
    root.mainloop()

main()
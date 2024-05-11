from math import factorial

class MathOperations:
    def ___init__(self):
        self.permutations_checkbox_value = IntVar()
        self.combinations_checkbox_value = IntVar()
        self.repeat_checkbox_value = IntVar()
        self.n = IntVar()
        self.k = IntVar()
        self.result_string = StringVar()


    def permutations_no_repeats(self, n:int, k:int) -> int:
        """Returns number of permutations possible where numbers cannot repeat"""
        non_repeat_permutations = (factorial(n.get())//factorial(n.get()-k.get()))
        result_string.set('Permutations without\nrepeat numbers:\n\n'+ str("{:,}".format(non_repeat_permutations)))
        #Callback to functions inside Gui class
        UI = Gui(primary=root)
        UI.update_result_label()
        UI.disable_combination_checkbox()

    def permutations_with_repeats(n:int, k:int) -> int:
        """Returns number of permutations possible where numbers can repeat"""
        repeat_permutations = (k.get()**n.get())
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

class UiFunctions:
    #Error Handling
    def validate_integer_input(self):
        """Displays error message if integer is not entered in either entries"""
        while True:
            try:
                n.get() == int or k.get() == int
            except Exception as e:
                e = 'n and k must be an integer'
                return messagebox.showerror('User Error', e)
            else:
                self.validate_positive_integer()
                break

    def validate_positive_integer(self):
        """Displays error message if integer is less than 0 in either entries"""
        while True:
            if n.get() <= -1 or k.get() <= -1:
                return messagebox.showerror('User error', 'Integer must be greater than 0')
            else:
                self.display_results()
                break

    def validate_float_integer(self):
        """Displays error message if float entered in either entries"""
        while True: 
            if float(n.get()) or float(k.get()):
                return messagebox.showerror('User Error', 'Integer cannot be float')
            else:
                self.display_results()
                break

    def selection_error_message(self):
        """Displays error message if permutations or combinatons checkbuttons state is not active"""
        if self.permutations_checkbox_value.get() == 0 and self.combinations_checkbox_value.get() == 0 and repeat_checkbox_value.get() == 0 or 1:
            messagebox.showerror('User Error', 'Please select Combinations or Permutations!')

    #output function
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
import math
import tkinter as tk
from tkinter import messagebox
from sympy import init_printing
from Basic_Operations import Operations
from Advance_methods import Adv_Methods
from differential_equations import DifferentialEqs
from linear_equations import Linear_Eqs, SystemOfEQs
from matriX import Matrix
from new_fractions import NewFractions
#from Laplace_ import Laplace_transforms

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(background='black')
root.resizable(width=False, height=False)
#allow a user to resizze the calc
root.geometry('450x550+450+100')
text_box = tk.Text(root, width=40, height=10)
text_box.pack()
#update_button = tk.Button(root, text="Update", command=update_textbox)
#update_textbox.pack()
calc = tk.Frame(root)
# calc.grid(row)
messagebox = messagebox

class Calculator_GUI():
    #initialize the event holders and the other modules that will be using
    def __init__(self, root):
        self.operations = Operations() 
        self.adv_methods = Adv_Methods()
        self.differential_eqs = DifferentialEqs()
        self.linear_eqs = Linear_Eqs()
        self.system_of_eqs = SystemOfEQs()
        self.matrix = Matrix()
        #self.matrix = None
        self.fractions = NewFractions()
        #self.laplace_calc = Laplace_transforms()

        self.root = root
        self.root.title('Scientific Calculator')
        self.root.configure(background='black')
        self.root.resizable(width=False, height=False)
        self.root.geometry('450x550+450+100')
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.txtDisplay = tk.Entry(self.root, font=('Helvetica', 20, 'bold'),
                                   bg='black', fg='white', bd=30, width=28, justify=tk.RIGHT)
        self.txtDisplay.grid(row=1, column=0, columnspan=4, pady=1)
        self.txtDisplay.insert(0, "0")
        self.equation = tk.Entry(root, width=36, borderwidth=5)
        self.equation.grid(row=1, column=0, columnspan=4)
        self.fraction_button = tk.Button(root, text="Fraction", command=self.fraction)
        self.fraction_button.grid(row=4, column=4)
        self.current=''
        self.user_input=True
        self.check_sum=False
        self.op=''
        self.result=False

        self.createButton()
    
    def fraction(self):
        user_input = self.entry_var.get()
        result = self.fractions.__add__(user_input)
        self.txtDisplay.delete(0, tk.END)
        self.txtDisplay.insert(0, result)
        
    def create_buttons(self):
        #create other button create code here....
        numberpad = "123456789"
        i=0
        btn = []
        
        for j in range(2,5):
            for k in range(3):
                btn.append(tk.Button(calc, width=6, height=2,
                                bg='black',fg='white',
                                font=('Helvetica',20,'bold'),
                                bd=4,text=numberpad[i]))
                btn[i].grid(row=j, column= k, pady = 1)
                btn[i]["command"]=lambda x=numberpad[i]:added_value.numberInput(x)
                i+=1

        special_buttons = [
        ("π", self.pi),
        ("+", self.add),
        ("-", self.subtract),
        ("*", self.multiply),
        ("/", self.divide),
        ("^", self.power),
        ("√", self.square_root),
        ("³√", self.cube_root),
        ("log", self.log),
        ("ln", self.log_base),
        ("±", self.negate),
        ("x²", self.square),
        ("x!", self.factorial),
        ("e^x", self.exponential),
        ("sin", self.sin),
        ("cos", self.cos),
        ("tan", self.tan),
        ("sin⁻¹", self.invsin),
        ("cos⁻¹", self.invcos),
        ("tan⁻¹", self.invtan),
        ("|x|", self.absolute_value)
        ]

        for j, (text, command) in enumerate(special_buttons, start=5):
            button = tk.Button(self.root, width=6, height=2, text=text, command=command)
            button.grid(row=j, column=(j - 5), pady=1)
    
    def numberInput(self, num):
        numniput_1 = txtDisplay.get()
        numniput_2 = str(num)
        if self.user_input:
            self.current = numniput_2
            self.user_unput = False
        else:
            if numniput_2 == '.':
                if numniput_2 in numniput_1:
                    return
            self.current = numniput_1 + numniput_2
        self.display(self.current)

    def perform_operation(self, operator):
        user_input = self.entry_var.get()
        current_number = float(user_input)
        self.current_operator = operator
        self.current_result = current_number

        self.entry_var.set("")
        #clears teh entry for the next number
    
    def calculate_result(self):
        user_input = self.entry_var.get()
        second_number = float(user_input)

        if self.current_operator == "+":
            result = self.operations.multiply(self.current_result, second_number)
            self.entry_var.set(result)
    
    def button_clicked(self, value):
            current_value = self.equation_entry.get()
            self.equation_entry.delete(0, tk.END)
            new_value = current_value + value
            self.equation_entry.insert(tk.END, new_value)

    def clearScreen(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.user_input=True

    def clearAllEntry(self):
        self.clearScreen()
        self.total=0
 
    def pi(self):
        self.result =  False
        self.current = math.pi
        self.update_display(self.current)
    
    def add(self):
        self.current = self.operations.add(self.current)
        self.update_display(self.current)
    
    def subtract(self):
        self.current = self.operations.subtract(self.current)
        self.update_display(self.current)

    def multiply(self):
        self.current = self.operations.multiply(self.current)
        self.update_display(self.current)

    def divide(self):
        self.current = self.operations.divide(self.current)
        self.update_display(self.current)

    def power(self):
        self.current = self.operations.power(self.current)
        self.update_display(self.current)

    def square_root(self):
        self.current = self.operations.square_root(self.current)
        self.update_display(self.current)

    def cube_root(self):
        self.current = self.operations.cube_root(self.current)
        self.update_display(self.current)
    
    def log_base(self):
        self.current = self.operations.log_base(self.current)
        self.display(self.current)
    
    def log(self):
        self.current = self.operations.log(self.current)
        self.display(self.current)

    def negate(self):
        self.current = self.operations.negate(self.current)
        self.display(self.current)

    def square(self):
        self.current = self.operations.square(self.current)
        self.display(self.current)

    def factorial(self):
        self.current = self.operations.factorial(self.current)
        self.display(self.current)

    def exponential(self):
        self.current = self.operations.exponential(self.current)
        self.display(self.current)
    
    def sin(self):
        self.current = self.operations.sin(self.current)
        self.display(self.current)
    
    def cos(self):
        self.current = self.operations.cos(self.current)
        self.display(self.current)

    def tan(self):
        self.current = self.operations.tan(self.current)
        self.display(self.current)

    def invcos(self):
        self.current = self.operations.invcos(self.current)
        self.display(self.current)
    
    def invsin(self):
        self.current = self.operations.invsin(self.current)
        self.display(self.current)

    def invtan(self):
        self.current = self.operations.invtan(self.current)
        self.display(self.current)
    
    def absolute_value(self):
        self.current = self.operations.absolute_value(self.current)
        self.display(self.current)

    # def solve_linear_equation(self):
    #     try:
    #         coefficients = [float(entry.get()) for entry in tk.Entry(self.x)]
    #         constant = float(txtDisplay.get())
    #         equation = Linear_Eqs(coefficients, constant)
    #         solution = equation.solve_for_variable()
    #         self.display(solution)
    #     except ValueError as e:
    #         self.display("Error: " + str(e))

    def input_matrix(self):
        mat = input(messagebox.showinfo("Input Matrix", "Please enter the matrix"))
        Matrix.input_matrix()
    
    def add_matrix(self, other):
        if self.matrix:
            Matrix.add_matrx(self, other)
        else:
            self.input_matrix()
    
    def multiply_matrix(self, other):
        if self.matrix:
            Matrix.matrix_multiply(self, other)
        else:
            self.input_matrix()

    def transpose_matrix(self):
        if self.matrix:
            Matrix.transpose(self)
        else:
            self.input_matrix()
    
    def ref(self):
        Matrix.row_echelon_form(self)
    
    def rref(self):
        Matrix.reduced_row_echelon_form(self)
        return Matrix.reduced_row
    
    def det(self):
        if self.matrix:
            Matrix.det(self)
        else:
            self.input_matrix() 

    def perform_adv_math(self):
        self.lower_lim = float(self.lower_lim_entry.get())
        self.upper_lim = float(self.upper_lim_entry.get())
        self.data = [float(x) for x in self.data_entry.get().split()]
        expression = self.expression_entry.get()
        self.num_interval = int(self.num_intervals_entry.get())
        self.step_size = float(self.step_size_entry.get())

        def_integration_result = self.adv_methods.def_integration()
        summation_result = self.adv_methods.summation(self.start, self.end, self.expression)
        mean_result = self.adv_methods.mean()
        median_result = self.adv_methods.median()
        mode_result = self.adv_methods.mode()
        riemann_sum_result = self.adv_methods.Riemann_sum(method='left') 

        self.result_label.config(text=f"Definite Integration: {def_integration_result}\n"
                                        f"Summation: {summation_result}\n"
                                        f"Mean: {mean_result}\n"
                                        f"Median: {median_result}\n"
                                        f"Mode: {mode_result}\n"
                                        f"Riemann Sum: {riemann_sum_result}")

        self.lower_lim_entry.delete(0, tk.END)
        self.upper_lim_entry.delete(0, tk.END)
        self.data_entry.delete(0, tk.END)
        self.expression_entry.delete(0, tk.END)
        self.num_intervals_entry.delete(0, tk.END)

    def add_frac(self, x, y):
        if isinstance(x, NewFractions) and isinstance(y, NewFractions):
            return NewFractions.__add__(x, y)
    
    def sub_frac(self, x, y):
        if isinstance(x, NewFractions) and isinstance(y, NewFractions):
            return NewFractions.__sub__(x, y)
    
    def mul_frac(self, x, y):
        if isinstance(x, NewFractions) and isinstance(y, NewFractions):
            return NewFractions.__mul__(x, y)
    
    # def laplace_transforms(self):
    #     equation_input = tk.simpledialog.askstring("Equation Input", "Enter an equation:")
    #     if equation_input:
    #         result_type, result = Laplace_transforms.calculate_transform(equation_input)
    #         self.display(f'{result_type}: {result}')
    #     else:
    #         self.display('No equation enterd')
    #     #display the result in the gui

    # def perform_Laplace_transforms(self):
    #     equation_input = tk.simpledialog.askstring("Equation Input", "Enter an equation:")
    #     if equation_input:
    #         result_type, result = Laplace_transforms.calculate_transform(equation_input)
    #         self.display(f'{result_type}: {result}')
    #     else:
    #         self.display('No equation enterd')
    #     #display the result in the gui

    

    def solve_equation(self):
        equation = self.equations_entry.get()
        solution = self.differential_solver.solve_differential_equation(equation)
        self.result_label.config(text=solution)

    def update_display(self, value):
            self.txtDisplay.delete(0, tk.END)
            self.txtDisplay.insert(0, value)

added_value = Calculator_GUI(root)

btnSolveLinear = tk.Button(calc, text="Solve Linear Equation", width=12,
                    height=3, bg='light blue',
                    font=('Helvetica', 12, 'bold'),
                    bd=4, command=Linear_Eqs.solve_linear_equation)
btnSolveLinear.grid(row=6, column=0, pady=1)

btnSolveSystem = tk.Button(calc, text="Solve System of Equations", width=12,
                        height=3, bg='light blue',
                        font=('Helvetica', 12, 'bold'),
                        bd=4, command=added_value.solve_system_of_equations)
btnSolveSystem.grid(row=6, column=1, pady=1)
# btnLaplace_Tranfm = tk.Button(calc, text="Laplace Transformation", width=12,
#                             height=3, bg='light blue',
#                             font=('Helvetica', 12, 'bold'),
#                             bd=4, command = Laplace_transforms.calculate_transform)
#                             #command=added_value.laplace_transformation)
# btnLaplace_Tranfm.grid(row=6, column=2, pady=1)
btnMatrix = tk.Button(calc, text="Input Matrix", width=12,
                      height= 3, bg='light blue',
                      font=('Helvetica', 12, 'bold'),
                      bd=4, command= Matrix.input_matrix)
#command=added_value.input_matrix)
        
txtDisplay = tk.Entry(calc, font=('Helvetica',20,'bold'),
            bg='black',fg='white',
            bd=30,width=28,justify=tk.RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

btnClear = tk.Button(calc, text=chr(67),width=6,
                height=2,bg='light blue',
                font=('Helvetica',20,'bold')
                ,bd=4, command=added_value.clearScreen
                ).grid(row=1, column= 0, pady = 1)
        
btnAllClear = tk.Button(calc, text=chr(67)+chr(69),
                    width=6, height=2,
                    bg='light blue',
                    font=('Helvetica',20,'bold'),
                    bd=4, command=added_value.clearAllEntry
                    ).grid(row=1, column= 1, pady = 1)

#btnDelete = tk.Button(calc, text="Delete", width=6, height=2,
                      
# btnADD = tk.Button(calc, text="+", width=6, height=2,
#                    bg = 'light blue', font = ('Helvetica',20,'bold'),
#                    bd = 4,
#                    command=added_value.add).grid(row=1, column= 2, pady = 1)

btnADD = tk.Button(calc, text='+', width=6, height=2, bg = 'light red', 
                   font=('Helvetica',20,'bold'), bd=4)
btnADD["command"] = lambda: added_value.add
btnADD.grid(row=1, column= 2, pady = 1)

btnSUB = tk.Button(calc, text="-", width=6, height=2,
                   bg = 'light blue', font = ('Helvetica',20,'bold'), bd = 4)
btnSUB["command"] = lambda: added_value.subtract
btnSUB.grid(row=1, column= 3, pady = 1)

btnMul = tk.Button(calc, text="*", width=6, height=2, bg = 'light blue',
                   font=('Helvetica',20,'bold'), bd = 4)
btnMul["command"] = lambda: added_value.multiply
btnMul.grid(row=1, column= 4, pady = 1)
'''
btnMUL = tk.Button(calc, text="*", width=6, height=2,
                   bg = 'light blue', font = ('Helvetica',20,'bold'),
                   bd = 4,
                   command=added_value.multiply).grid(row=1, column= 4, pady = 1)'''

btnDIV = tk.Button(calc, text="/", width=6, height=2, bg = 'light blue',
                   font=('Helvetica',20,'bold'), bd = 4)
btnDIV["command"] = lambda: added_value.divide
btnDIV.grid(row=1, column= 5, pady = 1)

btnDot = tk.Button(calc, text=".", width=6, height=2, bg = 'light blue',
                   font=('Helvetica',20,'bold'), bd = 4)
btnDot["command"] = lambda: added_value.numberInput('.')

btnEqual = tk.Button(calc, text="=", width=6, height=2, bg = 'light blue',
                     font=('Helvetica',20,'bold'), bd = 4)
btnEqual["command"] = lambda: added_value.equal
btnEqual.grid(row=1, column= 6, pady = 1)

btnPWR = tk.Button(calc, text="^", width=6, height=2,
                   bg='light blue', font = ('Helvetica',20,'bold'), bd = 4)
btnPWR["command"] = lambda: added_value.power
btnPWR.grid(row=1, column= 6, pady = 1)




# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

lblDisplay = tk.Label(calc, text = "Scientific Calculator",
                    font=('Helvetica',30,'bold'),
                    bg='black',fg='white',justify=tk.CENTER)
lblDisplay.grid(row=0, column= 4,columnspan=4)

def isExit():
    isExit = messagebox.askyesno("Scientific Calculator",
                                 "Do you want to exit?")
    if isExit>0:
        root.destroy()
        return
 
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("945x568+0+0") 
 
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = tk.Menu(calc)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = isExit)

root.config(menu=menubar)


print('test 68')
print('test 69')
print('test 70')

def main():
    root = tk.Tk()
    calc_gui = Calculator_GUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
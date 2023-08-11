import tkinter as tk

root = tk.Tk()
root.title ("Calculator")

e = tk.Entry(root, width = 35, borderwidth= 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#creating the button
def button_click(number):
    #e.delete(0,tk.END)
    current = e.get() #this allows to have teh numbers be next to each other without replacing
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)
    #whatever is in the display will be cleared

def button_add(): #need a way for the calculator to rember what i wrote in and add in to what isnext
    f_num = e.get()
    global fr_num 
    global math
    math = "addition"
    fr_num = int(f_num)
    e.delete(0, tk.END)  


def button_equal(): #it know
    sec_num = e.get() #pulls whats in the textbox
    e.delete(0, tk.END)
    if math == "addition":
        e.insert(0, fr_num + int(sec_num))  #want to nisert the answer
    if math == "subtraction":
        e.insert(0, fr_num - int(sec_num))
    if math == "multiplication":
        e.insert(0, fr_num * int(sec_num))
    if math == "division":
        e.insert(0, fr_num / int(sec_num))

def button_subtract():
    f_num = e.get()
    global fr_num 
    global math
    math = 'subtraction'
    fr_num = int(f_num)
    e.delete(0, tk.END)  

def button_multiplication():
    f_num = e.get()
    global fr_num 
    global math
    math = 'multiplicatiom'
    fr_num = int(f_num)
    e.delete(0, tk.END)

def button_division():
    f_num = e.get()
    global fr_num 
    global math
    math = 'division'
    fr_num = int(f_num)
    e.delete(0, tk.END)


button_1 = tk.Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = tk.Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = tk.Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = tk.Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = tk.Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = tk.Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = tk.Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = tk.Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = tk.Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = tk.Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = tk.Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_subtract = tk.Button(root, text = "-", padx = 42, pady = 20, command = button_subtract)
button_multiplication = tk.Button(root, text = "*", padx = 41, pady = 20, command = button_multiplication)
button_division = tk.Button(root, text = "/", padx = 41, pady = 20, command = button_division)

button_equal = tk.Button(root, text = "=", padx = 85, pady = 20, command = button_equal)
button_clear = tk.Button(root, text = "Clear", padx = 59, pady = 20, command= button_clear)

#placing the buttons on the screen
#tring to match how it looks on the app/physical calculator
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan= 3)
button_subtract.grid(row = 6, column=0)
button_multiplication.grid(row = 6, column=1)
button_division.grid(row = 6, column=2)
root.mainloop()

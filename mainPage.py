from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import os
import mat_calc

global root
root = tk.Tk()

root.title("lingebra main page")

mainFrame = ttk.Frame(root, relief= 'sunken', borderwidth= 50, width= 500, height = 400)

mainFrame.grid(row= 0, column=0)

path = os.path.dirname(os.path.abspath(__file__))
welcome_pic = ImageTk.PhotoImage(Image.open(path + '\Python.png').resize((200, 200)))
welcome_Message = ttk.Label(mainFrame, text= "welcome to lingebra", image= welcome_pic)
welcome_Message.grid(row= 0, column= 0, pady= 15)

def run_mat_calc() :
    Matrix_calc['state'] = tk.DISABLED
    exec(open(path +"\mat_calc.py").read())

global Matrix_calc
Matrix_calc = tk.Button(mainFrame, text= "Matrix calcultor", width= 18, command= run_mat_calc)
Matrix_calc.grid(row= 1, column= 0)

root.mainloop()




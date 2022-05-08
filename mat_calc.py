from turtle import back
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from mainPage import root, Matrix_calc


#below is the implemantation of the main window
global mainWindow
mainWindow = tk.Toplevel(root)
mainWindow.geometry('500x550')

#implementation of oporations
operation_frame = tk.Frame(mainWindow, width= 100, height= 250, borderwidth= 5, relief= 'sunken', background= '#626262')
operation_frame.grid(row=0, column=0)
operation_frame.grid_propagate(0)

matrix_sum_button = tk.Button(operation_frame,width=11, borderwidth= 5,relief= 'raised', text= "Matrix Sum")
matrix_sum_button.grid(row=0, column=0)

matrix_mult_button = tk.Button(operation_frame,width=11, borderwidth= 5,relief= 'raised', text= "Matrix Mult")
matrix_mult_button.grid(row=1, column=0)




def close_command():
    Matrix_calc['state'] = tk.NORMAL
    mainWindow.destroy()

mainWindow.protocol("WM_DELETE_WINDOW",  close_command)



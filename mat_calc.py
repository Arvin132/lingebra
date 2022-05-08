from turtle import back, title
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from mainPage import root, Matrix_calc
from Matrix import Matrix


#below is the implemantation of the main window
global mainWindow
mainWindow = tk.Toplevel(root)
mainWindow.geometry('500x300')

#implementation of oporations
operation_frame = tk.Frame(mainWindow, width= 100, height= 250, borderwidth= 5, relief= 'sunken', background= '#626262')
operation_frame.grid(row=1, column=0)
operation_frame.grid_propagate(0)

matrix_sum_button = tk.Button(operation_frame,width=11, borderwidth= 5,relief= 'raised', text= "Matrix Sum")
matrix_sum_button.grid(row=0, column=0)

matrix_mult_button = tk.Button(operation_frame,width=11, borderwidth= 5,relief= 'raised', text= "Matrix Mult")
matrix_mult_button.grid(row=1, column=0)


#matrix list frame, the frame that holds the list of matrixes
mat_list_frame = tk.Frame(mainWindow, width= 400, height= 250, borderwidth=5, relief= 'sunken', background= '#6F6F6F')
mat_list_frame.grid(row=1, column=1)
mat_list : list[Matrix] = []
def update_mat_frame():
    i = 0
    for matrix in mat_list:
        tk.Button(mat_list_frame, width= 25, borderwidth= 5,relief= 'raised', text= matrix.name).grid(column= 0, row= i)
        i += 1
#tool set frame
tool_set_frame = tk.Frame(mainWindow, width= 500, height= 50, borderwidth=5, relief= 'sunken', background= '#9A9A9A')
tool_set_frame.grid(row=0, column=0, columnspan= 2)





def close_command():
    Matrix_calc['state'] = tk.NORMAL
    mainWindow.destroy()

mainWindow.protocol("WM_DELETE_WINDOW",  close_command)



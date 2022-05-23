from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from Matrix import Matrix
from mainPage import root, Matrix_calc


#below is the implemantation of the main window
global mainWindow
mainWindow = tk.Toplevel(root)
mainWindow.geometry('500x300')

#implementation of oporations
operation_frame = tk.Frame(mainWindow, 
                           width= 100, 
                           height= 250, 
                           borderwidth= 5, 
                           relief= 'sunken',
                           background= '#626262')

operation_frame.grid(row=1, column=0)
operation_frame.grid_propagate(0)

matrix_sum_button = tk.Button(operation_frame, 
                              width=11, 
                              borderwidth= 5,
                              relief= 'raised', 
                              text= "Matrix Sum")
matrix_sum_button.grid(row=0, column=0)

matrix_mult_button = tk.Button(operation_frame, 
                               width=11,
                               borderwidth= 5,
                               relief= 'raised',
                               text= "Matrix Mult")
matrix_mult_button.grid(row=1, column=0)


#matrix list frame, the frame that holds the list of matrixes
global mat_list_frame
mat_list_frame = tk.Frame(mainWindow, 
                          width= 400, 
                          height= 250, 
                          borderwidth=5, 
                          relief= 'sunken', 
                          background= '#6F6F6F')
mat_list_frame.grid(row=1, column=1)
mat_list_frame.grid_propagate(False)

m1 = Matrix(rows= 3, columns= 3)
m1.update_row([1,2,3],1)
m1.update_row([4,5,6],2)
m1.update_row([7,8,9],3)
m1.name = "A"
m2 = Matrix(rows= 3, columns= 3)
m2.update_row([1,2,3],1)
m2.update_row([4,5,6],2)
m2.update_row([7,8,9],3)
m2.name = "B"
m3 = Matrix(rows= 3, columns= 3)
m3.update_row([1,2,3],1)
m3.update_row([4,5,6],2)
m3.update_row([7,8,9],3)
m3.name = "C"
mat_list : list[Matrix] = [m1,m2,m3,m1, m2]
mat_button_list : list[tk.Button] = []

def update_mat_frame(mat_list: list[Matrix], but_list: list[tk.Button]):
    i = 0
    j = 0
    for matrix in mat_list:
        bt =tk.Button(mat_list_frame, 
                      width= 12 , 
                      borderwidth= 4,
                      relief= 'raised', 
                      text= matrix.name)
        bt.grid(column=j, row=i)
        but_list.append(bt)
        j += 1
        if (j == 4):
            j = 0
            i += 1

def clear_mat_frame(but_list: list[tk.Button] = mat_button_list):
    for button in but_list:
        button.grid_remove()
    but_list.clear()

update_mat_frame(mat_list, mat_button_list)



#tool set frame
tool_set_frame = tk.Frame(mainWindow, 
                          width= 500, 
                          height= 50, 
                          borderwidth=5, 
                          relief= 'sunken', 
                          background= '#9A9A9A')
tool_set_frame.grid_propagate(False)
tool_set_frame.grid(row=0, column=0, columnspan= 2)

def mat_add_but_func():
    new = tk.Toplevel(mainWindow)
    new.geometry("250x200")

    rows = ttk.Entry(new,
                     width= 10)
    row_label = ttk.Label(new,
                          text="Rows:",
                          width= 5)
    row_label.grid(row=0, column=0)
    rows.grid(column=1, row=0)
    columns = ttk.Entry(new,
                        width= 10)
    column_label = ttk.Label(new,
                          text="Columns:",
                          width= 8)
    column_label.grid(row=0, column=2)
    columns.grid(column=3, row=0)

    cancel = tk.Button(new,
                        text="Cancel",
                        command= lambda : new.destroy(),
                        width= 10,
                        height= 3)
    cancel.grid(row= 4, column= 3, sticky= (tk.S, tk.E),
                pady= 100) 
add_mat_button = tk.Button(tool_set_frame, 
                           width= 10, 
                           height= 2,
                           text= "NEW",
                           command= mat_add_but_func)
add_mat_button.grid(row=0, column=0)



#this code edits what will happend when the top level is closed
def close_command():
    Matrix_calc['state'] = tk.NORMAL
    mainWindow.destroy()
mainWindow.protocol("WM_DELETE_WINDOW",  close_command)



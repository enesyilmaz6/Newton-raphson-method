# Newton Raphson
import pandas as pd
import sympy as sp
import numpy as np
import os

x = sp.Symbol("x") # we decided variable
func_list = []
tfunc_list = []
func = input("Function : ")
func = sp.sympify(func) # string transform function
tfunc = func.diff(x) # derivative func

bnok = [] # start point
bnok.append(float(input("Starting Point: ")))

iterasyon = int(input("İteration number: ")) # iteration number

func_list.append(func.subs(x,bnok[0])) # first function value
tfunc_list.append(tfunc.subs(x,bnok[0])) # first derivative function value
array = np.ones((iterasyon+1,5)) # created array with numpy
array[0][0] = bnok[0] # first column -> starting point
array[0][1] = func_list[0] # second column -> function value
array[0][2] = tfunc_list[0] # third column -> derivative function value
array[0][3] = func_list[0] / tfunc_list[0] # fourth column -> array[w][1] / array[w][2]
array[0][4] = bnok[0] - (func_list[0] / tfunc_list[0]) # fifth column array[w][0] - array[w][3]

for w in range(1,iterasyon+1): # loop return iteration times
    array[w][0] = array[w-1][4]
    array[w][1] = func.subs(x,array[w][0])
    array[w][2] = tfunc.subs(x,array[w][0])
    array[w][3] = array[w][1] / array[w][2]
    array[w][4] = array[w][0] - (array[w][1] / array[w][2])
    func_list.append(array[w][1])
    tfunc_list.append(array[w][2])
    bnok.append(array[w][0])

dataframe = pd.DataFrame(array,columns=["x[w]","f(x)","f'(x)","f(x)/f'(x)","x[w+1]"]) # array transfer dataframe
writer = pd.ExcelWriter("NRresult.xlsx") # write same directory
dataframe.to_excel(writer,'Sheet1') 
writer.save() # save 
os.startfile("NRresult.xlsx") # run excel file

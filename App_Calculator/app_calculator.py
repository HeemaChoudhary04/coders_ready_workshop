# -*- coding: utf-8 -*-
"""app calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kao0nnMb3fQK6NHqRIYFKhGC66HJzWKV
"""

pip install tkinter

list1 = ['Gopal',8.59,256,'True',[1,2,3]]
tuples =('Gopal',8.59,256,'True',[1,2,3])
set={'Gopal', 'Heema' , 'Hardeep','Gopal'}
dict1 = {'Name':'Hardeep', 'Roll no': '45'}

list1

print(list1,(0))

set

dict1

temp =[]
 temp1 =[]
 temp2 =[]
for i in range(10):
  a = i**2#a me save hui hai values
  b = i
  c = i**3
 temp.append(a)
 temp1.append(b)
 temp2.append(c)

temp

import matplotlib.pyplot as plt
plt.plot(temp,temp1, temp,temp2)

def add(a,b):
  return(a,b)

add(250,557)

from tkinter import *

expression =""

def press(num):
  global expression

  #expression = expression + str(num) OR
  expression += str(num)

  equation.set(expression)#if u dont want to repeat value 1st do set method and then convert it to your value


def equalpress():
   try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
   except:

      equation.set("Error")

      expression = ""


def clear():
    global expression

    expression  =""

    equation.set("")





    if __name__ == "__main__":
      gui = Tk()

      gui.configure(background = 'black')

      gui.title("Coders Ready")

      gui.geometry("270x150")

      equation = StringVar()


      expression_fields = Enter(gui, textvariable = equation)

      expression_field.grid(columnspan=4, ipadx=70)

      button1 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(1), height = 1 , width = 7)
      button1.grid(row =2, column =0)

      button2 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(2), height = 1 , width = 7)
      button2.grid(row =2, column =1)

      button3 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(3), height = 1 , width = 7)
      button3.grid(row =2, column =2)

      button4 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(4), height = 1 , width = 7)
      button4.grid(row =3, column =0)

      button5 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(5), height = 1 , width = 7)
      button5.grid(row =3, column =1)

      button6 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(6), height = 1 , width = 7)
      button6.grid(row =3, column =2)

      button7 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(7), height = 1 , width = 7)
      button7.grid(row =4, column =0)

      button8 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(8), height = 1 , width = 7)
      button8.grid(row =4, column =1)

      button9 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(9), height = 1 , width = 7)
      button9.grid(row =4, column =2)

      button0 = Button(gui, text = " 1 " , fg='black', bg = 'red', 
                       command = lambda: press(0),height=1 ,width=7) 
      plus = Button(gui, text= "+", fg ='black', bg ='red',
                    command = lambda: press('+'), height =1 ,width =7)
      plus.grid(row = 2,column = 3)
      minus = Button(gui, text= "-", fg ='black', bg ='red',
                    command = lambda: press('-'), height =1 ,width =7)
      minus.grid(row = 3,column = 3)   
      multiply = Button(gui, text= "*", fg ='black', bg ='red',
                    command = lambda: press('*'), height =1 ,width =7)
      multiply.grid(row = 4,column = 3) 
      divide = Button(gui, text= "/", fg ='black', bg ='red',
                    command = lambda: press('/'), height =1 ,width =7)
      divide.grid(row = 5,column = 3)   
      equal = Button(gui, text= "=", fg ='black', bg ='red',
                    command = lambda: press('='), height =1 ,width =7)
      equal.grid(row = 5,column = 2)   
      clear = Button(gui, text= "Clear", fg ='black', bg ='red',
                    command = clear, height =1 ,width =7)
      clear.grid(row = 5,column = 1)
      decimal = Button(gui, text= ".", fg ='black', bg ='red',
                    command = lambda: press('.'), height =1 ,width =7)
      decimal.grid(row = 6,column = 0)
     #start mainloop
      gui.mainloop()
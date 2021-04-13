from tkinter import*
from tkinter.ttk import*
import math

mathEq=""
sum=0

def button_click(userClick):
    global mathEq
    mathEq += userClick
    #update_screen()
    return

def button_equals_click():
    global mathEq
    global sum
    sum=mathEq.replace('×','*')
    sum=sum.replace('÷','/')
    sum=eval(sum)
    print(mathEq)
    if sum.is_integer():
        sum = int(sum)
    print('=',sum)
    return

def button_clear_click():
    global mathEq
    mathEq=""
    return
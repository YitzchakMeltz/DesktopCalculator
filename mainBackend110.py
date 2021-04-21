from tkinter import*
from tkinter.ttk import*
import math
from fractions import*

mathEq=""
sum=0

def button_click(userClick):
    global mathEq
    mathEq += userClick
    print(mathEq)
    return

def button_equals_click():
    global mathEq
    global sum
    sum=mathEq.replace('×','*')
    sum=sum.replace('÷','/')
    
    if sum == "":
        return

    try:
        sum=eval(sum)
    except (SyntaxError):
        sum="    Equation was not entered correctly"
        return

    print(mathEq)

    if isinstance(sum, int):
        sum = int(sum)
    else:
        try:
            sum=Fraction(str(sum)).limit_denominator()
        except (ValueError):
            sum="    Equation was not entered correctly"
        return


    print('=',sum)
    return

def button_clear_click():
    global mathEq
    mathEq=""
    return

def button_backspace_click():
    global mathEq

    # check that string of equation isn't empty
    if len(mathEq) == 0:
        return
    
    # remove white space before and after math operators
    # assume that white space can only be entered before and after a math operator
    if mathEq[-1] == " ":
        mathEq = mathEq[:-3]
        return

    # remove last character entered
    mathEq = mathEq[:-1]
    return
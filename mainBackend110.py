from tkinter import*
from tkinter.ttk import*
import math
from fractions import*

mathEq=""      # initialize the equation string
sum=0          # initialize the numerical sum

#--------------------------------------------------------------------
# function that is activated when user inputs a char that builds the equation

def button_click(userClick):
    global mathEq

    # add what the user clicked to the equation string
    mathEq += userClick

    # print current equation string for debugging purposes
    print(mathEq)
    return

#--------------------------------------------------------------------
# function that is activated when equals button is clicked

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

#--------------------------------------------------------------------
# function that is activated when the AC button is clicked
# Resets the math equation string to an empty string

def button_clear_click():
    global mathEq
    mathEq=""
    return

#--------------------------------------------------------------------
# function that is activated when the backspace button is clicked
# removes the last character that's in the equation (FILO)

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

#--------------------------------------------------------------------
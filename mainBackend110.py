from tkinter import*
from tkinter.ttk import*
import math
from fractions import*

mathEq=""      # initialize the equation string
sum=0          # initialize the numerical sum
decimalSum=""

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
    global decimalSum


    # replace user math operator symbols with programing operating operators
    sum=mathEq.replace('×','*')
    sum=sum.replace('÷','/')
    
    # if the string with the equation is empty, the function is finished
    if sum == "":
        return

    # evaluate the equation
    try:
        sum=eval(sum)
    except (SyntaxError):
        sum="    Equation was not entered correctly"
        decimalSum=""
        return

    #check if it is a float of type 2.0 etc. if it is - convert to integer
    if isinstance(sum, float):
        if sum.is_integer():
            sum = int(sum)


    # print the math equation to the console for debugging purposes
    print(mathEq)

    # check if result is an integer or a fraction
    if isinstance(sum, int):
        sum = int(sum)
        decimalSum=""
    else:
        try:
            decimalSum="   or   " + str(sum)
            sum=Fraction(str(sum)).limit_denominator()
        except (ValueError):
            sum="    Equation was not entered correctly"
            decimalSum=""
        return

    # print the solution to the console for debugging purposes
    print('=',sum)
    return

#--------------------------------------------------------------------
# function that is activated when the AC button is clicked
# Resets the math equation string to an empty string
# Resets the decimal sum string to an empty string

def button_clear_click():
    global mathEq, decimalSum
    mathEq=""
    decimalSum=""
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
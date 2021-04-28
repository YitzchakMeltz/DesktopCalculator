from tkinter import*
from tkinter.ttk import*
import math
from fractions import*

mathEq=""      # initialize the equation string
sum=0          # initialize the numerical sum
decimalSum=""

mathOperationSymbols = ["+","-","×","÷"]

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

def button_backspace_click(cursorPos):
    global mathEq

    # check that string of equation isn't empty and that cursor isn't at beginning of equation
    if len(mathEq) == 0 or cursorPos == 0:
        return cursorPos
    
    # remove white space before and after math operators
    # assume that white space can only be entered before and after a math operator
    if mathEq[(cursorPos - 1)] == " ":

        # invalid space was entered (theres no character before this space)
        if cursorPos < 2:
            return cursorPos

        # if cursor is in front of operator's space (such as " + ") then then remove operator and spaces
        if mathEq[(cursorPos - 2)] in mathOperationSymbols:
            mathEq = mathEq[:(cursorPos - 3)] + mathEq[cursorPos:]
            
            if cursorPos > 3 and mathEq[cursorPos - 4] == " ":
                return (cursorPos - 4)
            return (cursorPos - 3)

        mathEq = mathEq[:(cursorPos - 2)] + mathEq[(cursorPos - 1):]

        if mathEq[cursorPos - 2] == " ":
                return (cursorPos - 3)
        return (cursorPos - 2)

    if mathEq[(cursorPos - 1)] in mathOperationSymbols:
        mathEq = mathEq[:(cursorPos - 2)] + mathEq[(cursorPos + 1):]
        return (cursorPos - 2)

    # remove number at Cursor Position
    mathEq = mathEq[:(cursorPos - 1)] + mathEq[cursorPos:]

    if cursorPos > 1 and mathEq[cursorPos - 2] == " ":
            return (cursorPos - 2)
    return (cursorPos - 1)

#--------------------------------------------------------------------
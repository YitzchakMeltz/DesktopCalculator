import math
from fractions import*

mathEq=""      # initialize the equation string
sum=0          # initialize the numerical sum
decimalSum=""
lastEqual = False
ans = 0

mathOperationSymbols = ["+","-","×","÷"]

#--------------------------------------------------------------------
# function that is activated when user inputs a char that builds the equation

def button_click(userClick, cursorPos):
    global mathEq, lastEqual, ans

    # clear screen if previous entry was equals operator
    if(lastEqual):
        button_clear_click()

    # initialize cursor position if the QLineEdit has the placeholder
    if mathEq == "":
        cursorPos = 0

    # add what the user clicked to the equation string based on cursor position

    # user adds to the equation from the end
    if len(mathEq) == cursorPos:
        
        # add previous answer to equation if equal button was just pressed
        if(lastEqual and userClick in mathOperationSymbols):
            mathEq = str(ans) + userClick

        mathEq += userClick
        # print current equation string for debugging purposes
        print(mathEq)
        lastEqual = False
        return cursorPos + len(userClick)
    
    # user adds to equation with cursor before math operation symbol 
    # e.g. " |+ "
    if cursorPos > 1:
        if mathEq[cursorPos - 1] == " " and (mathEq[cursorPos - 2] not in mathOperationSymbols):
            mathEq = mathEq[:cursorPos - 1] + userClick + mathEq[cursorPos - 1:]
            return (cursorPos - 1) + len(userClick)

        if mathEq[cursorPos - 1] in mathOperationSymbols:
            mathEq = mathEq[:cursorPos + 1] + userClick + mathEq[cursorPos + 1:]
            return (cursorPos + 1) + len(userClick)

    if cursorPos == 1 and mathEq[cursorPos] in mathOperationSymbols:
        mathEq = mathEq[:0] + userClick + mathEq[0:]
        return len(userClick)

    mathEq = mathEq[:cursorPos] + userClick + mathEq[cursorPos:]
    return cursorPos + len(userClick)

#--------------------------------------------------------------------
# function that is activated when equals button is clicked

def button_equals_click():
    global mathEq, sum, decimalSum, lastEqual, ans

    lastEqual = True

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

    # store answer for future use
    ans = sum

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
    global mathEq, decimalSum, lastEqual
    mathEq=""
    decimalSum=""
    return

#--------------------------------------------------------------------
# function that is activated when the backspace button is clicked
# removes the last character that's in the equation (FILO)

def button_backspace_click(cursorPos):
    global mathEq, lastEqual

    lastEqual = False

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
import math
from fractions import*
from PyQt5.QtWidgets import QApplication

# try import for internet access test
try:
    import httplib
except:
    import http.client as httplib

class SagyLogic:

    def __init__(self):
        self.mathEq=""      # initialize the equation string
        self.sum=0          # initialize the numerical sum
        self.decimalSum=""
        self.lastEqual = False
        self.typingActive = True     # flag for active typing (for history)
        self.ans = 0
        self.historyStack = [""]   # initialize the history stack
        self.redoStack = []      # initialize the redo stack
        self.mathOperationSymbols = ["+","-","×","÷"]

    #--------------------------------------------------------------------
    # function that is activated when user inputs a char that builds the equation

    def button_click(self, userClick, cursorPos, cursorNotActive):

        self.typingActive = True
        self.redoStack = []
        
        # if cursor is active then disable lastEqual so that enables editing equation
        if(not cursorNotActive):
            self.lastEqual = False

        # clear screen if previous entry was equals operator
        if(self.lastEqual and cursorNotActive):
            self.clear()

        # initialize cursor position if the QLineEdit has the placeholder
        if self.mathEq == "":
            cursorPos = 0

        # add what the user clicked to the equation string based on cursor position

        # user adds to the equation from the end
        if len(self.mathEq) == cursorPos:
            
            # add previous answer to equation if equal button was just pressed
            if(self.lastEqual and cursorNotActive):
                if(len(userClick) == 3 and userClick[1] in self.mathOperationSymbols):
                    self.mathEq = str(self.ans) + userClick
                    self.lastEqual = False
                    return cursorPos + len(userClick) + len(str(self.ans))

            self.mathEq += userClick
            # print current equation string for debugging purposes
            print(self.mathEq)
            self.lastEqual = False
            return cursorPos + len(userClick)
        
        # user adds to equation with cursor before math operation symbol 
        # e.g. " |+ "
        if cursorPos > 1:
            if self.mathEq[cursorPos - 1] == " " and (self.mathEq[cursorPos - 2] not in self.mathOperationSymbols):
                self.mathEq = self.mathEq[:cursorPos - 1] + userClick + self.mathEq[cursorPos - 1:]
                return (cursorPos - 1) + len(userClick)

            if self.mathEq[cursorPos - 1] in self.mathOperationSymbols:
                self.mathEq = self.mathEq[:cursorPos + 1] + userClick + self.mathEq[cursorPos + 1:]
                return (cursorPos + 1) + len(userClick)

        if cursorPos == 1 and self.mathEq[cursorPos] in self.mathOperationSymbols:
            self.mathEq = self.mathEq[:0] + userClick + self.mathEq[0:]
            return len(userClick)

        self.mathEq = self.mathEq[:cursorPos] + userClick + self.mathEq[cursorPos:]
        return cursorPos + len(userClick)

    #--------------------------------------------------------------------
    # function that is activated when equals button is clicked

    def button_equals_click(self, settings):

        self.lastEqual = True
        self.typingActive = False

        stackChanged = False

        if self.historyStack[-1] != self.mathEq:
            self.historyStack.append(self.mathEq)    # add equation to history stack
            stackChanged = True
        
        if len(self.historyStack) > 10:
            self.historyStack.pop(0)
        print("Stack Size: ",len(self.historyStack))

        # replace user math operator symbols with programing operating operators
        self.sum=self.mathEq.replace('×','*')
        self.sum=self.sum.replace('÷','/')
        self.sum=self.sum.replace('%','/100')

        if "()" in self.sum:
            self.sum="    Equation was not entered correctly"
            self.decimalSum=""
            return
        
        # if the string with the equation is empty, the function is finished
        if self.sum == "":
            return

        # remove unnecessary zeros: i.e. '05090 + 0004' => '5090 + 4'
        self.sum = self.removeExtraZeros(self.sum)

        # evaluate the equation
        try:
            self.sum=eval(self.sum)
        except ZeroDivisionError:
            self.sum="    Cannot divide a number by zero"
            self.decimalSum=""
            return
        except (SyntaxError):
            self.sum="    Equation was not entered correctly"
            self.decimalSum=""
            return

        self.sum = (round(self.sum,15))    # round to help solve floating point aritmetic error

        #check if it is a float of type 2.0 etc. if it is - convert to integer
        if isinstance(self.sum, float):
            if self.sum.is_integer():
                self.sum = int(self.sum)

        # store answer for future use and copy to clipboard
        self.ans = self.sum
        if settings["CopyToClipboard"]:
            QApplication.clipboard().setText(str(round(self.sum,settings["decimalsToCopy"])))

        # print the math equation to the console for debugging purposes
        print(self.mathEq)

        # check if result is an integer or a fraction
        if isinstance(self.sum, int):
            self.sum = int(self.sum)
            self.decimalSum=""
        else:
            try:
                self.decimalSum="   or   " + str(self.sum)
                self.sum=Fraction(str(self.sum)).limit_denominator()
            except (ValueError):
                self.sum="    Equation was not entered correctly"
                self.decimalSum=""
            return

        # print the solution to the console for debugging purposes
        print('=',self.sum)

        return stackChanged

    #--------------------------------------------------------------------
    # function that is activated when the AC button is clicked
    # Resets the math equation string to an empty string
    # Resets the decimal sum string to an empty string

    def button_clear_click(self):
        if self.lastEqual:
            self.typingActive = True
        else:
            if self.historyStack[-1] != self.mathEq:
                self.historyStack.append(self.mathEq)
        self.mathEq=""
        self.decimalSum=""
        self.lastEqual = False
        self.redoStack = []
        return

    #--------------------------------------------------------------------
    # function that is activated by program when need to clear
    # Resets the math equation string to an empty string
    # Resets the decimal sum string to an empty string

    def clear(self):
        self.mathEq=""
        self.decimalSum=""
        return

    #--------------------------------------------------------------------
    # function that is activated when the backspace button is clicked
    # removes the last character that's in the equation (FILO)

    def button_backspace_click(self, cursorPos):

        self.redoStack = []
        self.lastEqual = False
        self.typingActive = True

        # check that string of equation isn't empty and that cursor isn't at beginning of equation
        if len(self.mathEq) == 0 or cursorPos == 0:
            return cursorPos
        
        # remove white space before and after math operators
        # assume that white space can only be entered before and after a math operator
        if self.mathEq[(cursorPos - 1)] == " ":

            # invalid space was entered (theres no character before this space)
            if cursorPos < 2:
                return cursorPos

            # if cursor is in front of operator's space (such as " + ") then then remove operator and spaces
            if self.mathEq[(cursorPos - 2)] in self.mathOperationSymbols:
                self.mathEq = self.mathEq[:(cursorPos - 3)] + self.mathEq[cursorPos:]
                
                if cursorPos > 3 and self.mathEq[cursorPos - 4] == " ":
                    return (cursorPos - 4)
                return (cursorPos - 3)

            self.mathEq = self.mathEq[:(cursorPos - 2)] + self.mathEq[(cursorPos - 1):]

            if self.mathEq[cursorPos - 2] == " ":
                    return (cursorPos - 3)
            return (cursorPos - 2)

        if self.mathEq[(cursorPos - 1)] in self.mathOperationSymbols:
            self.mathEq = self.mathEq[:(cursorPos - 2)] + self.mathEq[(cursorPos + 1):]
            return (cursorPos - 2)

        # remove number at Cursor Position
        self.mathEq = self.mathEq[:(cursorPos - 1)] + self.mathEq[cursorPos:]

        if cursorPos > 1 and self.mathEq[cursorPos - 2] == " ":
                return (cursorPos - 2)
        return (cursorPos - 1)

    #--------------------------------------------------------------------
    # function that is activated when the cursor arrow button is clicked
    def button_arrow_click(self, cursorPos, direction):
        if (direction == 'R' and cursorPos == len(self.mathEq)) or (direction == 'L' and cursorPos == 0):
            return cursorPos

        if(direction == 'R'):
            if self.mathEq[(cursorPos)] == " ":
                return (cursorPos + 3)
            if self.mathEq[(cursorPos)] in self.mathOperationSymbols:
                return (cursorPos + 2)
            if len(self.mathEq) == (cursorPos + 1) or self.singleSpaceSymbol(self.mathEq[(cursorPos)]):
                return (cursorPos + 1)

        if(direction == 'L'):
            if self.mathEq[(cursorPos - 1)] == " ":
                return (cursorPos - 3)
            if self.mathEq[(cursorPos - 1)] in self.mathOperationSymbols:
                return (cursorPos - 2)
            if self.singleSpaceSymbol(self.mathEq[(cursorPos - 1)]):
                return (cursorPos - 1)

    # Function that takes in a string and checks if it's a non space symbol that is not a math symbol
    def singleSpaceSymbol(self, str):
        if str in self.mathOperationSymbols:
            return False
        
        if str == " ":
            return False

        return True

    def get_previous_answer(self):
        return str(self.ans)

    #--------------------------------------------------------------------
    # Function that takes in a string and removes any zeros that are a 
    # prefix to a number
    # i.e. 004 => 4
    # Uses tail recursion
    @staticmethod
    def removeExtraZeros(str):
        def removeExtraZerosInner(str, afterNumber):
            if len(str) == 1:
                return str[0]

            if len(str) == 0:
                return ""

            if str[0] == ".":
                return str

            if str[0]=='0' and str[1].isnumeric() and not afterNumber:
                return  removeExtraZerosInner(str[1:],afterNumber)

            if str[0].isnumeric():
                return str[0] + removeExtraZerosInner(str[1:],True)

            return str[0] + removeExtraZerosInner(str[1:],False)

        return removeExtraZerosInner(str,False)

    @staticmethod
    def percentToDecimal(value):
        if value == "Auto":
            return "Auto"
        return str(float(value[:-1])/100)

    def handle_history(self, value):
        if value == "undo":
            if not self.typingActive:
                self.redoStack.append(self.mathEq)
                self.historyStack.pop()
                self.mathEq = self.historyStack[-1]
            else:
                self.typingActive = False
                self.redoStack.append(self.mathEq)
                self.mathEq = self.historyStack[-1]
            print("undo:", self.historyStack)
            print("redo:", self.redoStack,"\n")
            
        if value == "redo":
            if not self.typingActive:
                self.mathEq = self.redoStack.pop()
                self.historyStack.append(self.mathEq)
            else:
                self.typingActive = False
                self.historyStack.append(self.mathEq)
                self.mathEq = self.redoStack.pop()
            print("undo:", self.historyStack)
            print("redo:", self.redoStack,"\n")

        self.lastEqual = False
    #--------------------------------------------------------------------
    # Function that checks for internet connection
    @staticmethod
    def have_internet():
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            print("Internet Connection Availible")
            return True
        except:
            conn.close()
            print("No Internet Connection Found")
            return False
    #--------------------------------------------------------------------  
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
        self.math_equation = ""       # initialize the equation string
        self.sum = 0                  # initialize the numerical sum
        self.decimal_sum = ""
        self.last_equal = False
        self.typing_active = True     # flag for active typing (for history)
        self.ans = 0
        self.undo_stack = [""]        # initialize the history stack
        self.redo_stack = []          # initialize the redo stack
        self.math_op_symbols = ["+","-","×","÷"]

    #--------------------------------------------------------------------
    # function that is activated when user inputs a char that builds the equation

    def button_click(self, user_click, cursor_position, cursor_not_active):

        self.typing_active = True
        self.redo_stack = []
        
        # if cursor is active then disable last_equal so that enables editing equation
        if(not cursor_not_active):
            self.last_equal = False

        # clear screen if previous entry was equals operator
        if(self.last_equal and cursor_not_active):
            self.clear()

        # initialize cursor position if the QLineEdit has the placeholder
        if self.math_equation == "":
            cursor_position = 0

        # add what the user clicked to the equation string based on cursor position

        # user adds to the equation from the end
        if len(self.math_equation) == cursor_position:
            
            # add previous answer to equation if equal button was just pressed
            if(self.last_equal and cursor_not_active):
                if(len(user_click) == 3 and user_click[1] in self.math_op_symbols):
                    self.math_equation = str(self.ans) + user_click
                    self.last_equal = False
                    return cursor_position + len(user_click) + len(str(self.ans))

            self.math_equation += user_click
            # print current equation string for debugging purposes
            print(self.math_equation)
            self.last_equal = False
            return cursor_position + len(user_click)
        
        # user adds to equation with cursor before math operation symbol 
        # e.g. " |+ "
        if cursor_position > 1:
            if self.math_equation[cursor_position - 1] == " " and (self.math_equation[cursor_position - 2] not in self.math_op_symbols):
                self.math_equation = self.math_equation[:cursor_position - 1] + user_click + self.math_equation[cursor_position - 1:]
                return (cursor_position - 1) + len(user_click)

            if self.math_equation[cursor_position - 1] in self.math_op_symbols:
                self.math_equation = self.math_equation[:cursor_position + 1] + user_click + self.math_equation[cursor_position + 1:]
                return (cursor_position + 1) + len(user_click)

        if cursor_position == 1 and self.math_equation[cursor_position] in self.math_op_symbols:
            self.math_equation = self.math_equation[:0] + user_click + self.math_equation[0:]
            return len(user_click)

        self.math_equation = self.math_equation[:cursor_position] + user_click + self.math_equation[cursor_position:]
        return cursor_position + len(user_click)

    #--------------------------------------------------------------------
    # function that is activated when equals button is clicked

    def button_equals_click(self, settings):

        self.last_equal = True
        self.typing_active = False

        stackChanged = False

        if self.undo_stack[-1] != self.math_equation:
            self.undo_stack.append(self.math_equation)    # add equation to history stack
            stackChanged = True
        
        if len(self.undo_stack) > 10:
            self.undo_stack.pop(0)
        print("Stack Size: ",len(self.undo_stack))

        # replace user math operator symbols with programing operating operators
        self.sum=self.math_equation.replace('×','*')
        self.sum=self.sum.replace('÷','/')
        self.sum=self.sum.replace('%','/100')

        if "()" in self.sum:
            self.sum="    Equation was not entered correctly"
            self.decimal_sum=""
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
            self.decimal_sum=""
            return
        except (SyntaxError):
            self.sum="    Equation was not entered correctly"
            self.decimal_sum=""
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
        print(self.math_equation)

        # check if result is an integer or a fraction
        if isinstance(self.sum, int):
            self.sum = int(self.sum)
            self.decimal_sum=""
        else:
            try:
                if settings["display_as_fraction"]:
                    self.decimal_sum="   or   " + str(self.sum)
                    self.sum=Fraction(str(self.sum)).limit_denominator()
                else:
                    self.decimal_sum=" or   " + str(Fraction(str(self.sum)).limit_denominator())
                    self.sum=self.sum
            except (ValueError):
                self.sum="    Equation was not entered correctly"
                self.decimal_sum=""
            return

        # print the solution to the console for debugging purposes
        print('=',self.sum)

        return stackChanged

    #--------------------------------------------------------------------
    # function that is activated when the AC button is clicked
    # Resets the math equation string to an empty string
    # Resets the decimal sum string to an empty string

    def button_clear_click(self):
        if self.last_equal:
            self.typing_active = True
        else:
            if self.undo_stack[-1] != self.math_equation:
                self.undo_stack.append(self.math_equation)
        self.math_equation=""
        self.decimal_sum=""
        self.last_equal = False
        self.redo_stack = []
        return

    #--------------------------------------------------------------------
    # function that is activated by program when need to clear
    # Resets the math equation string to an empty string
    # Resets the decimal sum string to an empty string

    def clear(self):
        self.math_equation=""
        self.decimal_sum=""
        return

    #--------------------------------------------------------------------
    # function that is activated when the backspace button is clicked
    # removes the last character that's in the equation (FILO)

    def button_backspace_click(self, cursor_position):

        self.redo_stack = []
        self.last_equal = False
        self.typing_active = True

        # check that string of equation isn't empty and that cursor isn't at beginning of equation
        if len(self.math_equation) == 0 or cursor_position == 0:
            return cursor_position
        
        # remove white space before and after math operators
        # assume that white space can only be entered before and after a math operator
        if self.math_equation[(cursor_position - 1)] == " ":

            # invalid space was entered (theres no character before this space)
            if cursor_position < 2:
                return cursor_position

            # if cursor is in front of operator's space (such as " + ") then then remove operator and spaces
            if self.math_equation[(cursor_position - 2)] in self.math_op_symbols:
                self.math_equation = self.math_equation[:(cursor_position - 3)] + self.math_equation[cursor_position:]
                
                if cursor_position > 3 and self.math_equation[cursor_position - 4] == " ":
                    return (cursor_position - 4)
                return (cursor_position - 3)

            self.math_equation = self.math_equation[:(cursor_position - 2)] + self.math_equation[(cursor_position - 1):]

            if self.math_equation[cursor_position - 2] == " ":
                    return (cursor_position - 3)
            return (cursor_position - 2)

        if self.math_equation[(cursor_position - 1)] in self.math_op_symbols:
            self.math_equation = self.math_equation[:(cursor_position - 2)] + self.math_equation[(cursor_position + 1):]
            return (cursor_position - 2)

        # remove number at Cursor Position
        self.math_equation = self.math_equation[:(cursor_position - 1)] + self.math_equation[cursor_position:]

        if cursor_position > 1 and self.math_equation[cursor_position - 2] == " ":
                return (cursor_position - 2)
        return (cursor_position - 1)

    #--------------------------------------------------------------------
    # function that is activated when the cursor arrow button is clicked
    def button_arrow_click(self, cursor_position, direction):
        if (direction == 'R' and cursor_position == len(self.math_equation)) or (direction == 'L' and cursor_position == 0):
            return cursor_position

        if(direction == 'R'):
            if self.math_equation[(cursor_position)] == " ":
                return (cursor_position + 3)
            if self.math_equation[(cursor_position)] in self.math_op_symbols:
                return (cursor_position + 2)
            if len(self.math_equation) == (cursor_position + 1) or self.singleSpaceSymbol(self.math_equation[(cursor_position)]):
                return (cursor_position + 1)

        if(direction == 'L'):
            if self.math_equation[(cursor_position - 1)] == " ":
                return (cursor_position - 3)
            if self.math_equation[(cursor_position - 1)] in self.math_op_symbols:
                return (cursor_position - 2)
            if self.singleSpaceSymbol(self.math_equation[(cursor_position - 1)]):
                return (cursor_position - 1)

    # Function that takes in a string and checks if it's a non space symbol that is not a math symbol
    def singleSpaceSymbol(self, str):
        if str in self.math_op_symbols:
            return False
        
        if str == " ":
            return False

        return True

    def get_previous_answer(self):
        if self.ans == 0:
            return ""
        return str(self.ans)

    #--------------------------------------------------------------------
    # Function that takes in a string and removes any zeros that are a 
    # prefix to a number
    # i.e. 004 => 4
    # Uses tail recursion
    @staticmethod
    def removeExtraZeros(str):
        def removeExtraZerosInner(str, after_number):
            if len(str) == 1:
                return str[0]

            if len(str) == 0:
                return ""

            if str[0] == ".":
                return str

            if str[0]=='0' and str[1].isnumeric() and not after_number:
                return  removeExtraZerosInner(str[1:],after_number)

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
            if not self.typing_active:
                self.redo_stack.append(self.math_equation)
                self.undo_stack.pop()
                self.math_equation = self.undo_stack[-1]
            else:
                self.typing_active = False
                self.redo_stack.append(self.math_equation)
                self.math_equation = self.undo_stack[-1]
            print("undo:", self.undo_stack)
            print("redo:", self.redo_stack,"\n")
            
        if value == "redo":
            if not self.typing_active:
                self.math_equation = self.redo_stack.pop()
                self.undo_stack.append(self.math_equation)
            else:
                self.typing_active = False
                self.undo_stack.append(self.math_equation)
                self.math_equation = self.redo_stack.pop()
            print("undo:", self.undo_stack)
            print("redo:", self.redo_stack,"\n")

        self.last_equal = False
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
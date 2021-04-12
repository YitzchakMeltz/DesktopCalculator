from tkinter import*
from tkinter.ttk import*
from mainBackend import*

window = Tk()

window.title('Calculator')

window.iconbitmap('CalcuatorIcon.ico') 

#window.state('zoomed')     //start the program with screen maximized

window.geometry("400x500")

#create a style object
style = Style()
style.configure('TButton', font= ('calibri', 15), height=7, width=7)

screen_output_style = Style()
screen_output_style.configure("SCREEN.TLabel", font="calibri", fontsize=55)

result_output_style = Style()
result_output_style.configure("RESULT.TLabel", font="calibri", fontsize=70)


button_mathOper_style = Style()
button_mathOper_style.configure('BUTMO.TButton',height=7, width=3, bg='black')

button_0_style = Style()
button_0_style.configure('BUT0.TButton',height=7, width=15)

button_clear_style = Style()
button_clear_style.configure('BUTAC.TButton',height=7, width=3,font= ('calibri', 15))

calculatorPlaceolder = "Enter your equation"
calculatorOutput = Label(window, text= calculatorPlaceolder, style="SCREEN.TLabel")
calculatorOutput.place(x=200,y=50,anchor=CENTER)

resultPlaceolder = ""
resultOutput = Label(window, text= resultPlaceolder, style="RESULT.TLabel")
resultOutput.place(x=196,y=100,anchor=CENTER)

#test button
def my_click():
    my_label = Label(window,text="Button test succesful").pack()
    return

def click_and_update(userClick):
    button_click(userClick)
    update_screen()
    return

def click_and_clear():
    button_clear_click()
    update_screen()
    resultOutput.configure(text="")
    return

def equal_click():
    button_equals_click()
    update_screen()
    return

def update_screen():
    import mainBackend
    calculatorOutput.configure(text=mainBackend.mathEq)
    return

def update_result_screen():
    import mainBackend
    button_equals_click()
    resultOutput.configure(text="= " + str(mainBackend.sum))
    return

button_0 = Button(window, text = "0", command = lambda:click_and_update("0"), style ='BUT0.TButton')
button_1 = Button(window, text = "1", command = lambda:click_and_update("1"))
button_2 = Button(window, text = "2", command = lambda:click_and_update("2"))
button_3 = Button(window, text = "3", command = lambda:click_and_update("3"))
button_4 = Button(window, text = "4", command = lambda:click_and_update("4"))
button_5 = Button(window, text = "5", command = lambda:click_and_update("5"))
button_6 = Button(window, text = "6", command = lambda:click_and_update("6"))
button_7 = Button(window, text = "7", command = lambda:click_and_update("7"))
button_8 = Button(window, text = "8", command = lambda:click_and_update("8"))
button_9 = Button(window, text = "9", command = lambda:click_and_update("9"))
button_equals = Button(window, text = "=", command = update_result_screen, style ='BUTMO.TButton')
button_dot = Button(window, text = ".", command = lambda:click_and_update("."))
button_plus = Button(window, text = "+", command = lambda:click_and_update("+"), style = 'BUTMO.TButton')
button_minus = Button(window, text = "-", command = lambda:click_and_update("-"), style = 'BUTMO.TButton')
button_mult = Button(window, text = "×", command = lambda:click_and_update("×"), style = 'BUTMO.TButton')
button_div = Button(window, text = "÷", command = lambda:click_and_update("÷"), style = 'BUTMO.TButton')
button_openpar = Button(window, text = "(", command = lambda:click_and_update("("), style = 'BUTMO.TButton')
button_closepar = Button(window, text = ")", command = lambda:click_and_update(")"), style = 'BUTMO.TButton')
button_clear = Button(window, text = "AC", command = click_and_clear, style = 'BUTAC.TButton')


button_0.place(x= 100,y=450, anchor=CENTER)
button_1.place(x=60,y=415, anchor=CENTER)
button_2.place(x=141,y=415, anchor=CENTER)
button_3.place(x=222,y=415, anchor=CENTER)
button_4.place(x=60,y=380, anchor=CENTER)
button_5.place(x=141,y=380, anchor=CENTER)
button_6.place(x=222,y=380, anchor=CENTER)
button_7.place(x=60,y=345, anchor=CENTER)
button_8.place(x=141,y=345, anchor=CENTER)
button_9.place(x=222,y=345, anchor=CENTER)
button_equals.place(x=326,y=450, anchor=CENTER)
button_dot.place(x=222,y=450, anchor=CENTER)
button_plus.place(x=284,y=380, anchor=CENTER)
button_minus.place(x=326,y=380, anchor=CENTER)
button_mult.place(x=284,y=415, anchor=CENTER)
button_div.place(x=326,y=415, anchor=CENTER)
button_openpar.place(x=284,y=345, anchor=CENTER)
button_closepar.place(x=326,y=345, anchor=CENTER)
button_clear.place(x=284,y=450, anchor=CENTER)


window.mainloop()
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

button_mathOper_style = Style()
button_mathOper_style.configure('BUTMO.TButton',height=7, width=3, bg='black')

button_0_style = Style()
button_0_style.configure('BUT0.TButton',height=7, width=15)

button_clear_style = Style()
button_clear_style.configure('BUTAC.TButton',height=7, width=3,font= ('calibri', 15))

#test button
def my_click():
    my_label = Label(window,text="Button test succesful").pack()
    return

button_0 = Button(window, text = "0", command = lambda:button_click("0"), style ='BUT0.TButton')
button_1 = Button(window, text = "1", command = lambda:button_click("1"))
button_2 = Button(window, text = "2", command = lambda:button_click("2"))
button_3 = Button(window, text = "3", command = lambda:button_click("3"))
button_4 = Button(window, text = "4", command = lambda:button_click("4"))
button_5 = Button(window, text = "5", command = lambda:button_click("5"))
button_6 = Button(window, text = "6", command = lambda:button_click("6"))
button_7 = Button(window, text = "7", command = lambda:button_click("7"))
button_8 = Button(window, text = "8", command = lambda:button_click("8"))
button_9 = Button(window, text = "9", command = lambda:button_click("9"))
button_equals = Button(window, text = "=", command = button_equals_click, style ='BUTMO.TButton')
button_dot = Button(window, text = ".", command = lambda:button_click("."))
button_plus = Button(window, text = "+", command = lambda:button_click("+"), style = 'BUTMO.TButton')
button_minus = Button(window, text = "-", command = lambda:button_click("-"), style = 'BUTMO.TButton')
button_mult = Button(window, text = "×", command = lambda:button_click("×"), style = 'BUTMO.TButton')
button_div = Button(window, text = "÷", command = lambda:button_click("÷"), style = 'BUTMO.TButton')
button_openpar = Button(window, text = "(", command = lambda:button_click("("), style = 'BUTMO.TButton')
button_closepar = Button(window, text = ")", command = lambda:button_click(")"), style = 'BUTMO.TButton')
button_clear = Button(window, text = "AC", command = button_clear_click, style = 'BUTAC.TButton')


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
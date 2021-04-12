from tkinter import*
from tkinter.ttk import*

window = Tk()

window.title('Calculator')

window.iconbitmap('PythonGUITestIcon.ico') 

#window.state('zoomed')

window.geometry("400x500")

#create a style object
style = Style()

style.configure('TButton', font= ('calibri', 15, 'bold'))

button_0 = Button(window, text = "0")
button_1 = Button(window, text = "1")
button_2 = Button(window, text = "2")
button_3 = Button(window, text = "3")
button_4 = Button(window, text = "4")
button_5 = Button(window, text = "5")
button_6 = Button(window, text = "6")
button_7 = Button(window, text = "7")
button_8 = Button(window, text = "8")
button_9 = Button(window, text = "9")
button_equals = Button(window, text = "=")
button_dot = Button(window, text = ".")
button_plus = Button(window, text = "+")
button_minus = Button(window, text = "-")
button_mult = Button(window, text = "×")
button_div = Button(window, text = "÷")

button_0.pack()
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()
button_5.pack()
button_6.pack()
button_7.pack()
button_8.pack()
button_9.pack()
button_equals.pack()
button_dot.pack()
button_plus.pack()
button_minus.pack()
button_mult.pack()
button_div.pack()

window.mainloop()
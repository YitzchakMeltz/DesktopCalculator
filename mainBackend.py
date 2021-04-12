mathEq=""

def button_click(userClick):
    global mathEq
    mathEq += userClick
    return

def button_equals_click():
    global mathEq
    print(mathEq)
    return

def button_clear_click():
    global mathEq
    mathEq=""
    return
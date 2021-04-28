equation = "3 + 4"

cur = 2

# cursor position  i-1             i
if equation[cur - 1] == " " and equation[cur - 2] != "+":
    equation = equation[:cur-1] + "5" + equation[cur-1:]

print(equation)

#print(equation[0])
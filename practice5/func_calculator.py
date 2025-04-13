def calculator(a, b, op):
    if op == "+":
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b

a = list()
for i in range(1, 6):
    a.append(calculator(i, i, "*"))
print(a)
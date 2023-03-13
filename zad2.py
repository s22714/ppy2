num1 = int(input("Podaj liczbe -> "))
num2 = int(input("Podaj liczbe -> "))
op = input("Podaj operator -> ")

if op == "+" :
    print(num1 + num2)
if op == "-" :
    print(num1 - num2)
if op == "/":
    print(num1 / num2)
if op == "%":
    print(num1 % num2)
if op == "*":
    print(num1 * num2)
if op == "^" or op == "**":
    print(num1 ** num2)
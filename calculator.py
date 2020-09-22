a = float(input())
zn = input()
b = float(input())
if zn == '+':
    print(a + b)
if zn == '-':
    print(a - b)
if zn == '*':
    print(a * b)
if zn == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
if zn == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
if zn == 'pow':
    print(a ** b)
if zn == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
        

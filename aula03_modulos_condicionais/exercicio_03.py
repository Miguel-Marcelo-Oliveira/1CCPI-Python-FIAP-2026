num1 = float(input("Digite um  número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2:
    print(f'{num1} é maior do que {num2}')
elif num1 < num2:
    print(f'{num2} é maior do que {num1}')
else:
    print(f'{num1} e {num2} são iguais')
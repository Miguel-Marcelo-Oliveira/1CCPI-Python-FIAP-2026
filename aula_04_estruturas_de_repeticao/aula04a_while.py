# cp = 0
# while cp < 10:
#     cp += 1
#     if cp == 3 or cp == 5:
#         continue
#     print(f'Produto {cp}')
#
#     if cp == 7:
#         break
#
# print()
# # While decrescente de 4 até 1
# i = 4
# while i > 0:
#     print(i)
#     i -= 1

def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente nota: "))
    return nota

notaA = float(input("Digite a 1ª nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a 2º nota: "))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2
print(media)
...

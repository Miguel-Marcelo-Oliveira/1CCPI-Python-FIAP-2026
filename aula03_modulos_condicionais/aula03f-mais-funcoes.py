# FUNÇÕES SEM RETORNO E COM PAR.

def boas_vindas(nome):
    print(f"Olá {nome}! Seja bem-vindo!")

nome_digitado = "João"
boas_vindas(nome_digitado)

# FUNÇÕES COM RETORNO E COM PARAM.
def soma (num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(2, 8)
print(resultado_soma)
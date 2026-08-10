lista_emails = ["joao.silva@fiap.com.br", "maria.souza@fiap.com.br", "ana.paula@fiap.com.br"]

dominios = []
usuarios = []

for email in lista_emails:
    nome_usuario, email = email.split("@")
    dominios.append(email)
    usuarios.append(nome_usuario)

usuarios_tupla = tuple(usuarios)
dominios_tupla = tuple(dominios)

def analisador(lista_de_emails):
    d = dict()
    for dom in dominios:
        if dom not in d:
            d[dom] = 1
        else:
            d[dom] += 1

    return d

def relatorio_final():
    print('-' * 30)
    print('RELATÓRIO COMPLETO')
    print('Quantidade de emails por domínio:')
    print(analisador(lista_emails))
    print(f'\nLista de usuários original: \n{usuarios}')
    print(f'\nTupla de usuários inverrtida: \n{usuarios_tupla[::-1]}')
    print('-' * 30)

relatorio_final()
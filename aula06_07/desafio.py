lista_emails = ["joao.silva@fiap.com.br", "maria.souza@fiap.com.br", "ana.paula@fiap.com.br"]

dominios = []
usuarios = []

for email in lista_emails:
    nome_usuario, email = email.split("@")
    dominios.append(email)
    usuarios.append(nome_usuario)
    d = dict()
    for dom in dominios:
        if dom not in d:
            d[dom] = len(dom)

usuarios = tuple(usuarios)
print(f'dommínio: {len(dominios)}')
print(f'usuários: {usuarios}')
print(d)
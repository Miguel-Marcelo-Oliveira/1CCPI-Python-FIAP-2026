from model import model_lead
import control

def add_nead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Etapa no funil de vendas: ")

    # validar os dados...
    # depois de valiado... precisamos modelar os dados
    # vamos modelar o lead como um dicionário
    print(model_lead(name,email,status))

    # depois do meu lead modelado como dict
    # precisamos enviar o dict para o leads.json
    # vamos usar o control para isso
    control.create_lead(model_lead(name,email,status))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)
    # formatar como tabela...

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Aicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do Programa")

        opt = input("Escolha uma opção: ")

        if opt =='1':
            add_nead()
            print("Lead adicionado")
        elif opt =='2':
            list_leads()
        elif opt =='0':
            print("Até mais...")
            break
        else:
            print("Opção iválida")

if __name__ == '__main__':
    main()
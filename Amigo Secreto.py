from email.message import EmailMessage
import ssl
import smtplib
import random

# Cria um dicionário com o nome das pessoas e o email delas
friend_email = {
    'Pedro': 'pedro@mail.com',
    'Nicolas': 'nicolas@mail.com',
    'Henrique': 'henrique@mail.com',
    'Guilherme': 'guilherme@mail.com',
    'Leonardo': 'leonardo@mail.com',
    'Jesse': 'jesse@mail.com',
    'Vinicius': 'vinicius@mail.com',
    'Vitor': 'vitor@mail.com',
    'Pedrox': 'pedrox@mail.com',
}

# Define o login e senha do email que enviará os emails para os indivíduos
email_sender = 'quem.envia@gmail.com'
email_password = 'ABCD ABCD ABCD ABCD'
subject = 'Amigo Secreto'

context = ssl.create_default_context()

def enviar_email(email_receiver, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def sorteio_amigo_secreto(friend_email):
    while True:
        sorteio = list(friend_email.keys())
        random.shuffle(sorteio)

        pares = list(zip(friend_email.keys(), sorteio))
        if all(a != b for a, b in pares) and not any((b, a) in pares for a, b in pares):
            return pares

def print_pares(pares):
    print("Resultado do Amigo Secreto:")
    for a, b in pares:
        print(f"{a} tirou {b}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Embaralhar e printar (sem enviar email)")
        print("2. Embaralhar e enviar email (sem printar)")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                pares = sorteio_amigo_secreto(friend_email)
                print_pares(pares)
            except Exception as e:
                print(f"Erro no sorteio: {e}")

        elif opcao == '2':
            try:
                pares = sorteio_amigo_secreto(friend_email)
                for i, pessoa in pares:
                    email_receiver = friend_email[i]
                    body = f'Seu amigo secreto é {pessoa}'
                    enviar_email(email_receiver, body)
            except Exception as e:
                print(f"Erro no sorteio: {e}")

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção Inválida!")
    
menu()

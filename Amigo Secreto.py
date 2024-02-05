from email.message import EmailMessage
import ssl
import smtplib
import random

# Cria um dicionário com o nome das pessoas e o email delas
friend_email = {
    'John': 'john.doe@mail.com',
    'Jane': 'jane.smith@mail.com',
    'Alex': 'alex.jonesy@mail.com',
    'Emily': 'emily.roberts@mail.com',
    'Daniel': 'daniel.williams@mail.com',
    'Olivia': 'olivia.jenkins@mail.com',
    'Sophie': 'sophie.davis@mail.com',
    'William': 'william.white@mail.com',
    'Eva': 'eva.bronx@mail.com',
}
# cria uma lista com aqueles que ja foram escolhidos
escolhidos = []

#define o login e senha do email que enviara os emails para os individuos
email_sender = 'quem.envia@gmail.com'
email_password = 'ABCD ABCD ABCD ABCD'

subject = 'Amigo Secreto'

context = ssl.create_default_context()
#loop para percorrer a lista 1 por 1 e enviar um email sem ninguém se pegar ou pegar repetido
for i in friend_email:
    while True:
        pessoa = random.choice(list(friend_email.keys()))
        if pessoa != i and pessoa not in escolhidos:
            email_receiver = friend_email[i]  # Set the receiver's email address
            body = f'Seu amigo secreto é {pessoa}'
            
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            escolhidos.append(pessoa)
            break


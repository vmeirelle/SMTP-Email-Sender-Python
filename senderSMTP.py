#Programa para enviar emails via protocolo SMTP

#Biblioteca protocolo SMPT
import smtplib

#Porta e servidor local
#Nescessário configuração de um servidor de email local (hMailServer)
#Servidor configurado no localhost, porta 25, dados dos usuários:
#login = 'user1@vmeirelle.lab'
#password = '123' 
#receiver = 'user2@vmeirelle.lab'

#Dados  do seu servidor:
port = 25 
smtp_server = 'localhost' 

try: 
    #Conexão do servidor.
    server = smtplib.SMTP(smtp_server, port)
    print('Servidor Alcançado, aguardando login do usuário . . .')
    #Entrada dos dados de usuário.
    login = input('Insira seu e-mail: ')
    password = input('Insira sua senha: ')
    try:
        #Login do usuário
        server.login(login, password)
        print('Login realizado com sucesso')

        #Insira os dados do destinatário e da mensagem:
        receiver = input('Digite seu destinatário: ')
        subject = input('Digite o assunto: ')
        messagebody = input('Digite a mensagem: ')
        message = f"""\
        Subject: {subject}
        To: {receiver}
        From: {login}

        {messagebody}"""
        try:
            #Envio da mensagem: 
            server.sendmail(login, receiver, message)
            print('Mensagem enviada. ')  
            server.close()
        except:
            print ('Erro ao enviar. ')
    except:
        print('Login não realizado, por favor tente novamente.')
except:
    print('Servidor não alcançado, por favor tente novamente.')





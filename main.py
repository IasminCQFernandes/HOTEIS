# criar banco de dados
# instalar pyodbc
import pyodbc
from datetime import datetime
import pyodbc
from datetime import datetime
import smtplib
import email.message  # No need to import 'email.message' module separately

# Rest of your code...

def enviar_email(nome_propriedade, data_checkin, data_checkout, diaria, total_dias, total):
    corpo_email = f"""
    <p>Reserva realizada! </br>Confirme seus dados: </br>Local: {nome_propriedade}</br>Check-in: {data_checkin}</br>Check-out: {data_checkout}</br>Valor diaria: {diaria}</br>Total de diarias: {total_dias}</br>Total a pagar: {total}<p>
    """

    msg = email.message.Message()  # This should work fine now
    msg['Subject'] = f"RESERVAS - {nome_propriedade}"
    msg['From'] = 'iasmincarolinefernandes@gmail.com'
    msg['To'] = 'iasmincarolinefernandes@gmail.com'
    password = 'iavefncmncsepmha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado!')






dados_conexao = (
    'Driver={SQL Server};'
    'Server=BHZ-SIS-0008;'
    'Database=Hospedagem;'
    
)

# criar conexao
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')

# criar cursor - executa os comandos
cursor = conexao.cursor()

def Registrar():
    nome = input('nome: ')
    email_reg = input('e-mail: ')
    telefone = int(input('telefone: '))
    senha = input('Senha: ')
    endereco = input('endereço: ')
    
    cursor.execute(f"""SELECT * FROM Clientes WHERE email = '{email_reg}'""")
    resultado = cursor.fetchone()
    
    if resultado:
        print("Este e-mail já está cadastrado.")
        print('Faça login')
        login()
    else: 
        if  len(senha) < 8:
            print('A senha deve ter no mínimo 8 caracteres. Tente novamente.')
        else: 
            comando = f"""INSERT INTO Clientes(nome, email, telefone, senha, endereco) values ('{nome}','{email_reg}','{telefone}',{senha}, '{endereco}')"""
            cursor.execute(comando)
            print('Usuario cadastrado!')
            login()
    
def login():
    global email_login
    email_login = input('E-mail: ') 
    senha = input('Senha: ')
    
    cursor.execute(f"""SELECT * FROM Clientes WHERE email = '{email_login}' AND senha = '{senha}'""")
    resultado = cursor.fetchone()
    
    if resultado:
        print('Login bem-sucedido!')
        
        Reservar()  
        return True
    else:
        print('Usuario não encontrado! Favor Registrar ou Recuperar senha!')
        decisao = input('Digite a opção desejada:\n[1] Registrar\n[2]Recupar Senha')
        if decisao == '1':
            Registrar()
        elif decisao == '2':
            rec_senha()
        else:
            print('Opção invalida!')
                
        return False
    

def rec_senha():
    email_senha = input('E-mail: ')
    cursor.execute(f"""SELECT * FROM Clientes WHERE email = '{email_senha}'""")
    resultado = cursor.fetchone()
    
    if resultado:
        nova_senha = input('Digite nova senha: ')
        if len(nova_senha) < 8:
            print('A senha deve ter no mínimo 8 caracteres.')
        else:
            cursor.execute(f"""UPDATE Clientes SET senha = '{nova_senha}' WHERE email = '{email_senha}'""")
            print('Senha trocada, realize o login!')
            login()
            return True
    else:
        print('Usuario não encontrado! Favor Registrar')
        Registrar()
                
        return False
    
    
# def Reservar(nome, email, telefone, ):

def Reservar():
    from datetime import datetime 
    nome_propriedade = input('Propriedade: ')
    data_checkin = input('entrada: ')
    data_checkout = input('saida: ')
    n_quartos = int(input('qtd quartos: '))
    # total = float(input('total: '))
    status = 1
    data_checkin_form = datetime.strptime(data_checkin, '%d/%m/%Y') 
    data_checkout_form = datetime.strptime(data_checkout, '%d/%m/%Y') 
    total_dias = (data_checkout_form - data_checkin_form).days
    diaria = 70
    total = total_dias * diaria * n_quartos
    
    
    cursor.execute(f"""SELECT id FROM Clientes WHERE email = '{email_login}'""")
    id_cliente = cursor.fetchone()[0]
    # print(id_cliente)
            
            
            
    cursor.execute(f"""SELECT id FROM Propriedades WHERE nome = '{nome_propriedade}'""")
    id_propriedade = cursor.fetchone()[0]
            
    # comando = f"""INSERT INTO Reservas(cliente_id, propriedade_id, data_checkin, data_checkout, numero_quartos, preco_total, status) values ({id_cliente},{id_propriedade},'{data_checkin}','{data_checkout}', {n_quartos},{total},'{status}')"""
    comando = f"""INSERT INTO Reservas(cliente_id, propriedade_id, data_checkin, data_checkout, numero_quartos, preco_total, status) values ({id_cliente},{id_propriedade},'{data_checkin}','{data_checkout}', {n_quartos},{total},'{status}')"""

    cursor.execute(comando)
    print('Reserva realizada com sucesso!')
    
    data_checkin = str(data_checkin)
    data_checkout = str(data_checkout)
    diaria = str(diaria)
    total_dias = str(total_dias)
    total = str(total)
    
    enviar_email(nome_propriedade, data_checkin, data_checkout, diaria, total_dias, total)
    
    
    
    
def Confirmar():
    id = int(input('Digite o ID da reserva a ser confirmada: '))
    cursor.execute(f"""UPDATE Reservas SET status = 2 WHERE id = '{id}'""")
    
def Cancelar():
    id = int(input('Digite o ID da reserva a ser confirmada: '))
    cursor.execute(f"""UPDATE Reservas SET status = 3 WHERE id = '{id}'""")
 
# def enviar_email(nome_propriedade, data_checkin, data_checkout, diaria, total_dias, total):
#     corpo_email = f"""
#     <p>Reserva realizada!\nConfirme seus dados:\nLocal: '{nome_propriedade}'\nCheck-in: '{data_checkin}'\nCheck-out: '{data_checkout}'\nValor diaria: '{diaria}'\nTotal de diarias: '{total_dias}'\nTotal a pagar: '{total}'<p>
#     """

#     msg = email.message.Message()
#     msg['Subject'] = "Dolar está abeixo de R$5,20"
#     msg['From'] = 'iasmincarolinefernandes@gmail.com'
#     msg['To'] = 'iasmincarolinefernandes@gmail.com'
#     password = 'iavefncmncsepmha'
#     msg.add_header('Content-Type', 'text/html')
#     msg.set_payload(corpo_email)
    
#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()
#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#     print('Email enviado!')
     
login() 
# caso haja alteração tem que dar o commit
cursor.commit()
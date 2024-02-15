# Sistema de Reserva de Propriedades 
Este é um sistema simples de reserva de propriedades desenvolvido em Python. Ele utiliza um banco de dados SQL Server para armazenar informações sobre clientes, propriedades e reservas.

- ## Funcionalidades
Registro de Usuário: Os usuários podem se registrar no sistema fornecendo informações como nome, e-mail, telefone, senha e endereço.

- ### Login de Usuário:
Os usuários registrados podem fazer login no sistema usando seu e-mail e senha.

- ### Recuperação de Senha: 
Os usuários podem recuperar sua senha fornecida por seu e-mail registrado.

- ### Reserva de Propriedades: 
Os usuários podem reservar uma propriedade especificando detalhes como nome da propriedade, datas de check-in e check-out, número de quartos, etc.

- ### Confirmação de Reserva: 
Os usuários podem confirmar uma reserva existente fornecida ou o ID da reserva.

- ### Cancelamento de Reserva: 
Os usuários podem cancelar uma reserva existente fornecida ou o ID da reserva.

- ### Envio de E-mail de Confirmação: 
Após a reserva de uma propriedade, um e-mail de confirmação é enviado para o endereço de e-mail do usuário.

## Pré-requisitos 
Python 3.x Bibliotecas Banco de dados SQL Server

## Instalação e Uso Instale das bibliotecas: ´
- pip install pyodbc 
- pip install DateTime 
- pip install secure-smtplib 
- pip install email 
- Execute o script Python main.py.

Siga as instruções no terminal para registrar-se, fazer login, reservar uma propriedade, confirmar ou cancelar uma reserva.

## Autores

- [@IasminFernandes](https://github.com/IasminCQFernandes)

Licença Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

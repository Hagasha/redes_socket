#Grupo composto por Arthur Narciso, Matheus Pena, Rayan Diniz e Vinicíus Alves.

#Importa o programa de rede socket
import socket

# Configuração do cliente
host = '127.0.0.1'
port = 12345

# Cria um socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client_socket.connect((host, port))

# Recebe a mensagem de boas-vindas do servidor
message = client_socket.recv(1024).decode()
print(f"Servidor diz: {message}")

while True:
    # Solicita ao usuário que insira uma mensagem
    message_to_server = input("Digite uma mensagem para o servidor (ou 'sair' para encerrar): ")
    
    if message_to_server.lower() == 'sair':
        break

    # Envia a mensagem para o servidor
    client_socket.send(message_to_server.encode())

# Fecha a conexão com o servidor
client_socket.close()

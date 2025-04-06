import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7001))
server_socket.listen(1)
print('с о п')
connection, address = server_socket.accept()
print(f'п к')
data = connection.recv(1024).decode()
print(f'о п в к')
if data == "INFO":
    connection.send("це чат від логаки!!".encode)
elif data == 'HELP':
    connection.send("доступні команди: HELP, INFO".encode())
else:
    connection.send("невідома команда". encode())
connection.send('привіт від сервера')
connection.close()
server_socket.close()
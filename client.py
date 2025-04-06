import socket

olient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

olient_socket.connect(('tcp://5.tcp.eu.ngrok.io', 14467))

msg = input("введіть повідомленя:")
olient_socket.send(msg.encode())

response = olient_socket.recv(1024).decode()
print(f'Відповідь від сервера: {response}')

olient_socket.close()


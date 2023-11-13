import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        message_2 = input("Enter your message as a server: ")
        client_socket.sendall(message_2.encode('utf-8'))
        data2 = client_socket.recv(1024)
        response2 = data.decode('utf-8')
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##Se declaran 2 sockets server_socket 1 de tipo AF_INET y otro de tipo SOCK_STREAM
    host = '127.0.0.1'  ##Se declara que el servidor va a ser el host con esa ip
    port = 12345  ##Se declara el puerto por donde el servidor va a recibir y enviar
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

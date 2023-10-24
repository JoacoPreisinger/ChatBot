import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1' ##Aca se especifica la ip al que el cliente se va a conectar
    port = 12345 ##Aca se especifica el puerto al que el cliente se va a conectar
    client_socket.connect((host, port)) ##Esto sirve para que el cliente se conecte a la ip y al puerto 

    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Server response: {response}")
        message2 = data.decode('utf-8')
        print(f"Received message: "+message2)
        client_socket.sendall(message2.encode('utf-8'))

if __name__ == "__main__":
    main()

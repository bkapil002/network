import socket

def start():
    server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soket.bind(('localhost' , 8080))
    server_soket.listen(1)
    print("server started and listening")

    client_soket , add = server_soket.accept()
    print(f"connection from{add}")

    data = client_soket.recv(1024)
    print(f"recever: {data.decode()}")

    client_soket.send(b"Hello from server")
    client_soket.close()

start()    
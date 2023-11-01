import socket

HOST = "127.0.0.1" 
PORT = 65432

#code from realpython.com/python-sockets
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Waiting for client connection...")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
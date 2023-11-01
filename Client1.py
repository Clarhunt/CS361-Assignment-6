import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

userInput = ""
while userInput != "1":
    userInput = input("Press 1 to send a message to the server: ")
    if(userInput !="1"):
        print("You didn't press 1 try again")
message = input("Enter the message you want to send to the server: ")
data = message.encode() #the message must be converted to bytes
print("Client 1 is attempting to access the server")

dataReceived = ""
#code from realpython.com/python-sockets
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)
    dataReceived = s.recv(1024)

dataReceived = dataReceived.decode() #puts the data back into a string
print("The following message was received: ", dataReceived)
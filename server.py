import socket 
import threading 

HREADER = 64
PORT = 5050
# Getting Local IPV4 IP Address 
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


#AF_INET = Stands for IPV4 type
# SOCK_STREAM = streaming data through the socket in the form of bytes 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) 

def handle_client(conn, addr):
    print("New Connection {addr} connected.") 
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length.decode(FORMAT)
        print(f"{addr}, {msg}")

def start():
    server.listen()
    while true: 
        # addr = address bound to the socket on the other end (PORT AND IP) INFO
        # conn = new socket object usable to send and rev data
        conn, addr = server.accept()
        # Runs handle_clinet func
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        thread.start()
        print(f"Active Connections {threading.activeCount() - 1}") 


print("Sever is starting.")
start()

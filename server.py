import socket 
import threading 

HREADER = 64
PORT = 5050
# Getting Local IPV4 IP Address 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNCTED!"



#AF_INET = Stands for IPV4 type
# SOCK_STREAM = streaming data through the socket in the form of bytes 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) 

def handle_client(conn, addr):
    #print(f"New Connection {addr} connected.") 
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"Server is listeing on {SERVER}")
    while True: 
        # addr = address bound to the socket on the other end (PORT AND IP) INFO
        # conn = new socket object usable to send and rev data
        conn, addr = server.accept()
        # Runs handle_clinet func
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        thread.start()
        print(f"Active Connections {threading.activeCount() - 1}") 


print("Sever is starting.")
start()

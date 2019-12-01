import socket
import threading
import time
      
class Server:


    def __init__(self, ip, port):
        self.socket = None
        self.clients = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen()
        
    def listen(self, player_amount): # listen for player_amount connections
        self.socket.listen(player_amount)
        for i in range(player_amount):
            conn, addr = self.socket.accept()
            conn.setblocking(0)
            self.clients.append(conn)
        self.socket.setblocking(0)
        self.broadcast("all clients in")
        self.receive()
        
    def send(self, client, msg): # send message to specific client
        print ("sending", msg, "to", client)
        client.sendall(msg.encode("utf-8"))
        
    def broadcast(self, msg): #send msg to all connections on server
        print ("broadcasting", msg)
        i = 0
        for client in self.clients:
            i += 1
            client.sendall(msg.encode("utf-8"))
        
    def receive(self): #receive list of messages from connections connected to server
        msg = b""
        for client in self.clients:
            try:
                while True:
                    data = client.recv(1024)
                    msg += data
            except socket.error:
                continue
        return msg.decode("utf-8")
        
        
        
def create_server(ip_addr, port, players):
    server = Server(ip_addr, port)
    server.listen(players)
    i = 0
    while True:
        messages = server.receive() # receive messages from active connections
        server.broadcast(str(i))
        i += 1
        time.sleep(1)
            
            
if __name__ == "__main__":
    h = "127.0.0.1"
    p = 65432
    create_server(h, p, 2)